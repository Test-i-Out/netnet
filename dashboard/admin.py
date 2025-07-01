from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import FirewallRule


@admin.register(FirewallRule)
class FirewallRuleAdmin(admin.ModelAdmin):
    list_display = ['rule_id', 'source', 'destination', 'service', 'action', 'created_at']
    list_filter = ['service', 'action', 'created_at']
    search_fields = ['rule_id', 'source', 'destination', 'service']
    ordering = ['rule_id']