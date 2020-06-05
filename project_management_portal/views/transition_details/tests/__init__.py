# pylint: disable=wrong-import-position

APP_NAME = "project_management_portal"
OPERATION_NAME = "transition_details"
REQUEST_METHOD = "get"
URL_SUFFIX = "transition/{task_id}/v1/"

from .test_case_01 import TestCase01TransitionDetailsAPITestCase

__all__ = [
    "TestCase01TransitionDetailsAPITestCase"
]
