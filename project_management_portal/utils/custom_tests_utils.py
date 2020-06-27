from django_swagger_utils.utils.test import CustomAPITestCase
from project_management_portal.models.factories import *


class CustomTestUtils(CustomAPITestCase):
    def setupUser(self, username, password):
        super(CustomTestUtils, self).setupUser(
            username=username, password=password
        )
        UserFactory.reset_sequence()
        StateFactory.reset_sequence()
        ChecklistFactory.reset_sequence()
        TransitionFactory.reset_sequence()
        WorkflowFactory.reset_sequence()
        ProjectFactory.reset_sequence()
        TaskFactory.reset_sequence()
