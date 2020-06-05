import pytest
import datetime
from freezegun import freeze_time
from project_management_portal.storages.project_storage_implementation \
    import ProjectStorageImplementation

@pytest.mark.django_db
@freeze_time("2020-05-20")
def test_create_project_storage_with_valid_details_return_project_details_dto(
    project_details_dto, create_users, create_workflow, create_project):

    # Arrange

    user_id = 1
    assigned_to = [1, 2]
    name = "project_management_portal"
    description = "The name of the project is project_management_portal"
    workflow_type = 1
    project_type = "CRM"

    storage = ProjectStorageImplementation()

    # Act
    response = storage.create_project(name=name,
                           user_id=user_id,
                           assigned_to=assigned_to,
                           description=description,
                           workflow_type=workflow_type,
                           project_type=project_type)

    # Assert
    assert response == project_details_dto