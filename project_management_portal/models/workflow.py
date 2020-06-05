from django.db import models

from project_management_portal.models.user import User

class Workflow(models.Model):
    name = models.CharField(max_length=100)
    states = models.ManyToManyField('State', related_name='workflows')

    transitions = models.ManyToManyField(
        'Transition', related_name='workflows')

    created_at = models.DateTimeField(auto_now=True)