from django.db import models
from project_management_portal.models.project import Project
from project_management_portal.constants.enums import IssueType


class Task(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()

    ISSUE_TYPE_CHOICE = (
        (IssueType.TASK.value, IssueType.TASK.value),
        (IssueType.BUG.value, IssueType.BUG.value),
        (IssueType.DEVELOPER_STORY.value, IssueType.DEVELOPER_STORY.value),
        (IssueType.USER_STORY.value, IssueType.USER_STORY.value),
        (IssueType.ENHANCEMENT.value, IssueType.ENHANCEMENT.value)
    )

    issue_type = models.CharField(
        max_length=20, choices=ISSUE_TYPE_CHOICE, default=None, null=True)

    project = models.ForeignKey(
        'Project', on_delete=models.CASCADE, related_name='tasks')

    state = models.ForeignKey('State',
                              on_delete=models.CASCADE,
                              related_name='tasks',
                              default='TODO')

    created_by_id = models.IntegerField()

    created_at = models.DateTimeField(auto_now=True)
