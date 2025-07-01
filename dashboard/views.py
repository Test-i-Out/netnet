from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib import messages
from django.db.models import Q
from .models import FirewallRule
import re


def index(request):
    """Main dashboard view"""
    query = request.GET.get('query', '')
    results = []
    query_successful = False
    
    if query:
        try:
            results = process_query(query)
            if results:
                query_successful = True
                messages.success(request, 'Query successful.')
            else:
                messages.info(request, 'Query executed successfully but no results found.')
        except Exception as e:
            messages.error(request, f'Query failed: {str(e)}')
    
    context = {
        'query': query,
        'results': results,
        'query_successful': query_successful,
    }
    
    return render(request, 'dashboard/index.html', context)


def process_query(query):
    query = query.lower().strip()
    queryset = FirewallRule.objects.all()

    # Match: show rules with source 10.1.1.0/24
    if query.startswith('show rules with source'):
        match = re.search(r'show rules with source\s+([\d./]+)', query)
        if match:
            source = match.group(1).strip()
            queryset = queryset.filter(source__iexact=source)

    # Match: show rules with destination 10.2.2.0/24
    elif query.startswith('show rules with destination'):
        match = re.search(r'show rules with destination\s+([\d./]+)', query)
        if match:
            destination = match.group(1).strip()
            queryset = queryset.filter(destination__iexact=destination)

    elif query.startswith('http'):
        queryset = queryset.filter(
            Q(service__icontains='http') | Q(service__icontains='https')
        )

    elif query.startswith('allow'):
        queryset = queryset.filter(action__iexact='allow')

    elif query.startswith('deny'):
        queryset = queryset.filter(action__iexact='deny')

    else:
        queryset = queryset.filter(
            Q(rule_id__icontains=query) |
            Q(source__icontains=query) |
            Q(destination__icontains=query) |
            Q(service__icontains=query) |
            Q(action__icontains=query)
        )

    return list(queryset)
