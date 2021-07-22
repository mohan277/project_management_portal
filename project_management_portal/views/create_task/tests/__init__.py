# pylint: disable=wrong-import-position

APP_NAME = "project_management_portal"
OPERATION_NAME = "create_task"
REQUEST_METHOD = "post"
URL_SUFFIX = "task/v1/"

from .test_case_01 import TestCase01CreateTaskAPITestCase
from .test_case_02 import TestCase02CreateTaskAPITestCase
from .test_case_03 import TestCase03CreateTaskAPITestCase

__all__ = [
    "TestCase01CreateTaskAPITestCase",
    "TestCase02CreateTaskAPITestCase",
    "TestCase03CreateTaskAPITestCase"
]
