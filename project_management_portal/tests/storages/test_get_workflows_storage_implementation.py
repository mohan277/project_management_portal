import pytest
import datetime
from freezegun import freeze_time
from project_management_portal.models import Project, Workflow, User
from django_swagger_utils.drf_server.exceptions import NotFound
from project_management_portal.storages.workflow_storage_implementation \
    import WorkflowStorageImplementation


@pytest.mark.django_db
@freeze_time("2020-05-20")
def test_get_workflows_storage_returns_list_of_workflows(
    create_workflow, get_workflows_expected_output):

    # Arrange
    storage = WorkflowStorageImplementation()

    # Act
    response = storage.get_list_of_workflows()

    # Assert
    assert response == get_workflows_expected_output
