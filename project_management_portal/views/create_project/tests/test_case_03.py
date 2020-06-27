"""
# TODO: Update test case description
"""

from freezegun import freeze_time
from django.utils import timezone
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


class TestCase03CreateProjectAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    @freeze_time('2020-06-21')
    def setupUser(self, username, password):
        super(TestCase03CreateProjectAPITestCase, self).setupUser(
            username=username, password=password
        )
        user = self.foo_user
        user.is_admin = True
        user.save()
        workflow = WorkflowFactory()
        ProjectFactory.create(workflow_type=workflow, created_by=user, created_at=timezone.now)


    def test_case(self):
        response = self.default_test_case()

        import json

        response_content = json.loads(response.content)

        project_id = response_content['project_id']

        project = Project.objects.get(id=project_id)

        self.assert_match_snapshot(
            name='name',
            value=project.name
        )
        self.assert_match_snapshot(
            name='description',
            value=project.description
        )
        self.assert_match_snapshot(
            name='workflow_type',
            value=project.workflow_type_id
        )
        self.assert_match_snapshot(
            name='project_type',
            value=project.project_type
        )
        self.assert_match_snapshot(
            name='created_by',
            value=project.created_by.id
        )
