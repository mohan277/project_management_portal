import pytest
import datetime
from freezegun import freeze_time
from project_management_portal.models import Project, Workflow, User
from django_swagger_utils.drf_server.exceptions import NotFound
from project_management_portal.storages.project_storage_implementation \
    import ProjectStorageImplementation
from project_management_portal.interactors.storages.dtos import \
    ListOfProjectsDto


@pytest.mark.django_db
@freeze_time("2020-05-20")
def test_get_admin_projects_storage_with_valid_detail_return_list_of_projects(
    create_project, get_admin_projects_expected_output):

    # Arrange
    user_id = 1
    limit = 3
    offset = 0
    storage = ProjectStorageImplementation()

    # Act
    response = storage.get_list_of_admin_projects(
        limit=limit, offset=offset, user_id=user_id
    )

    # Assert
    assert response == get_admin_projects_expected_output


@pytest.mark.django_db
@freeze_time("2020-05-20")
def test_get_member_projects_storage_with_valid_detail_return_list_of_projects(
    create_project, get_member_projects_expected_output):

    # Arrange
    user_id = 2
    limit = 3
    offset = 0
    storage = ProjectStorageImplementation()

    # Act
    response = storage.get_list_of_member_projects(
        limit=limit, offset=offset, user_id=user_id
    )

    # Assert
    assert response == get_member_projects_expected_output
