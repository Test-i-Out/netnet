from django.core.management.base import BaseCommand
from dashboard.models import FirewallRule


class Command(BaseCommand):
    help = 'Populate database with sample firewall rules'

    def handle(self, *args, **options):
        # Clear existing rules
        FirewallRule.objects.all().delete()
        
        # Sample rules matching the screenshot
        sample_rules = [
            {
                'rule_id': '1001',
                'source': '10.1.1.0/24',
                'destination': '10.2.2.0/24',
                'service': 'HTTP',
                'action': 'Allow'
            },
            {
                'rule_id': '1002',
                'source': '10.1.1.0/24',
                'destination': '10.3.3.0/24',
                'service': 'HTTPS',
                'action': 'Deny'
            },
            {
                'rule_id': '1003',
                'source': '10.1.1.0/24',
                'destination': '10.4.4.0/24',
                'service': 'SSH',
                'action': 'Allow'
            },
            {
                'rule_id': '1004',
                'source': '10.1.1.0/24',
                'destination': '10.5.5.0/24',
                'service': 'ICMP',
                'action': 'Allow'
            },
            # Additional rules for testing
            {
                'rule_id': '1005',
                'source': '192.168.1.0/24',
                'destination': '10.0.0.0/8',
                'service': 'FTP',
                'action': 'Deny'
            },
            {
                'rule_id': '1006',
                'source': '172.16.0.0/16',
                'destination': '10.2.2.0/24',
                'service': 'HTTP',
                'action': 'Allow'
            },
        ]
        
        for rule_data in sample_rules:
            FirewallRule.objects.create(**rule_data)
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {len(sample_rules)} firewall rules')
        )