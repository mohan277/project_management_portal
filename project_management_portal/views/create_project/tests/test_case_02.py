"""
# TODO: Update test case description
"""

from project_management_portal.models import Project
from project_management_portal.models.factories import WorkflowFactory, \
    ProjectFactory, UserFactory
from project_management_portal.utils.custom_tests_utils import CustomTestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "name": "string",
    "description": "string",
    "workflow_type": 1,
    "project_type": "Classic Software"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["write"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase02CreateProjectAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE


    def setupUser(self, username, password):
        super(TestCase02CreateProjectAPITestCase, self).setupUser(
            username=username, password=password
        )
        workflow = WorkflowFactory()
        # user = UserFactory()


    def test_case(self):
        self.default_test_case() # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.

