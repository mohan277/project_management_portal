from django.db import models
from project_management_portal.models.checklist import Checklist

class Transition(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    from_state = models.ForeignKey(
        'State', on_delete=models.CASCADE, related_name='state_transitions')

    to_state = models.ForeignKey(
        'State', on_delete=models.CASCADE, related_name='transitions')

    checklist = models.ManyToManyField(Checklist)




















































































