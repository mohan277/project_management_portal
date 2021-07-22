"""
# TODO: Update test case description
"""

from project_management_portal.models import Task
from project_management_portal.models.factories import TaskFactory, \
    ProjectFactory
from project_management_portal.utils.custom_tests_utils import CustomTestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


REQUEST_BODY = """
{
    "project": 1,
    "state": 1,
    "title": "string",
    "description": "string",
    "issue_type": "Task"
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


class TestCase01CreateTaskAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE


    def setupUser(self, username, password):
        super(TestCase01CreateTaskAPITestCase, self).setupUser(
            username=username, password=password
        )

        # project = ProjectFactory()
        TaskFactory()


    def test_case(self):
        response = self.default_test_case()

        import json

        response_content = json.loads(response.content)

        task_id = response_content['task_id']

        task = Task.objects.get(id=task_id)

        self.assert_match_snapshot(
            name='title',
            value=task.title
        )
        self.assert_match_snapshot(
            name='description',
            value=task.description
        )
        self.assert_match_snapshot(
            name='project',
            value=task.project_id
        )
        self.assert_match_snapshot(
            name='state',
            value=task.state_id
        )
        self.assert_match_snapshot(
            name='created_by',
            value=task.created_by_id
        )
