import pytest
import datetime
from freezegun import freeze_time
from project_management_portal.models import Project, Workflow
from django_swagger_utils.drf_server.exceptions import NotFound
from project_management_portal.storages.task_storage_implementation \
    import TaskStorageImplementation
from project_management_portal.interactors.storages.dtos import \
    ListOfTasksDto


@pytest.mark.django_db
@freeze_time("2020-05-20")
def test_get_tasks_storage_with_valid_details_returns_list_of_tasks(
        create_task, create_project, get_tasks_expected_output):

    # Arrange
    project_id = 1
    storage = TaskStorageImplementation()

    # Act
    response = storage.get_list_of_tasks(
        project_id=project_id)

    # Assert
    assert response == get_tasks_expected_output


@pytest.mark.django_db
@freeze_time("2020-05-20")
def test_get_tasks_storage_with_no_data(no_tasks_expected_output):

    # Arrange
    project_id = 1
    storage = TaskStorageImplementation()

    # Act
    response = storage.get_list_of_tasks(
        project_id=project_id)

    # Assert
    assert response == no_tasks_expected_output
