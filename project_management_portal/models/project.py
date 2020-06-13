from django.db import models
from project_management_portal.constants.enums import ProjectType
from project_management_portal.models.user import User
from project_management_portal.models.workflow import Workflow


class Project(models.Model):
    name = models.CharField(max_length=100)

    workflow_type = models.ForeignKey(
        'Workflow', on_delete=models.CASCADE, related_name='projects')

    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    PROJECT_CHOICE = (
        (ProjectType.CLASSICSOFTWARE.value, ProjectType.CLASSICSOFTWARE.value),
        (ProjectType.FINANCIAL.value, ProjectType.FINANCIAL.value),
        (ProjectType.CRM.value, ProjectType.CRM.value)
    )

    project_type = models.CharField(
        max_length=20, choices=PROJECT_CHOICE, default=None, null=True)

    created_by = models.ForeignKey(
        'User', on_delete=models.CASCADE, related_name='admin_projects')

    assigned_to = models.ManyToManyField('User', related_name='member_projects')


    class Meta:
        ordering = ['-created_at']˜˜