# pylint: disable=wrong-import-position

APP_NAME = "project_management_portal"
OPERATION_NAME = "list_of_states"
REQUEST_METHOD = "get"
URL_SUFFIX = "states/{task_id}/v1/"

from .test_case_01 import TestCase01ListOfStatesAPITestCase
from .test_case_02 import TestCase02ListOfStatesAPITestCase
from .test_case_03 import TestCase03ListOfStatesAPITestCase
from .test_case_04 import TestCase04ListOfStatesAPITestCase

__all__ = [
    "TestCase01ListOfStatesAPITestCase",
    "TestCase02ListOfStatesAPITestCase",
    "TestCase03ListOfStatesAPITestCase",
    "TestCase04ListOfStatesAPITestCase"
]
