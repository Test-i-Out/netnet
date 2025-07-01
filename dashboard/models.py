from django.db import models

# Create your models here.
from django.db import models


class FirewallRule(models.Model):
    rule_id = models.CharField(max_length=50, unique=True)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    service = models.CharField(max_length=50)
    action = models.CharField(max_length=20, choices=[
        ('Allow', 'Allow'),
        ('Deny', 'Deny'),
        ('Drop', 'Drop'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['rule_id']

    def __str__(self):
        return f"Rule {self.rule_id}: {self.source} -> {self.destination} ({self.action})"