"""
# TODO: Update test case description
"""

from project_management_portal.models import Transition
from project_management_portal.models.factories import TransitionFactory
from project_management_portal.utils.custom_tests_utils import CustomTestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "name": "string",
    "description": "string",
    "from_state": "string",
    "to_state": "string"
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


class TestCase01CreateTransitionAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase01CreateTransitionAPITestCase, self).setupUser(
            username=username, password=password
        )
        TransitionFactory()

    def test_case(self):
        response = self.default_test_case()

        import json

        response_content = json.loads(response.content)

        transition_id = response_content['transition_id']

        transition = Transition.objects.get(id=transition_id)

        self.assert_match_snapshot(
            name='name',
            value=transition.name
        )
        self.assert_match_snapshot(
            name='description',
            value=transition.description
        )
        self.assert_match_snapshot(
            name='from_state',
            value=transition.from_state
        )
        self.assert_match_snapshot(
            name='to_state',
            value=transition.to_state
        )
