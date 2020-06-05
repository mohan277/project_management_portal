# pylint: disable=wrong-import-position

APP_NAME = "project_management_portal"
OPERATION_NAME = "list_of_workflows"
REQUEST_METHOD = "get"
URL_SUFFIX = "workflows/v1/"

from .test_case_01 import TestCase01ListOfWorkflowsAPITestCase

__all__ = [
    "TestCase01ListOfWorkflowsAPITestCase"
]
