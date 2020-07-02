from project_management_portal.models.project import Project
from project_management_portal.models.workflow import Workflow
from project_management_portal.models.state import State
from project_management_portal.models.transition import Transition
from project_management_portal.models.task import Task
from project_management_portal.models.checklist import Checklist
from project_management_portal.models.developer import Developer


__all__ = [
    "Project",
    "Workflow",
    "State",
    "Transition",
    "Task",
    "Checklist",
    "Developer"
]

# class DummyModel(AbstractDateTimeModel):
#     """
#     Model to store key value pair
#     Attributes:
#         :var key: String field which will be unique
#         :var value: String field which will be of 128 char length
#     """
#     key = models.CharField(max_length=128, unique=True)
#     value = models.CharField(max_length=128)
#
#     class Meta(object):
#         app_label = 'sample_app'
#
#     def __str__(self):
#         return "<DummyModel: {key}-{value}>".format(key=self.key,
#                                                     value=self.value)
#
