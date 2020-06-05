# pylint: disable=wrong-import-position

APP_NAME = "project_management_portal"
OPERATION_NAME = "list_of_tasks"
REQUEST_METHOD = "get"
URL_SUFFIX = "project/tasks/{project_id}/v1/"

from .test_case_01 import TestCase01ListOfTasksAPITestCase

__all__ = [
    "TestCase01ListOfTasksAPITestCase"
]
