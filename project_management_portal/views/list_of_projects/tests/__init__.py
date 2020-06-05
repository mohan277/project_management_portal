# pylint: disable=wrong-import-position

APP_NAME = "project_management_portal"
OPERATION_NAME = "list_of_projects"
REQUEST_METHOD = "get"
URL_SUFFIX = "projects/v1/"

from .test_case_01 import TestCase01ListOfProjectsAPITestCase

__all__ = [
    "TestCase01ListOfProjectsAPITestCase"
]
