import pytest
import datetime
from freezegun import freeze_time
from project_management_portal.models import Project, Task, State
from project_management_portal.storages.task_storage_implementation \
    import TaskStorageImplementation


@pytest.mark.django_db
@freeze_time("2020-05-20")
def test_create_task_storage_with_valid_details_return_task_details_dto(
    create_project, task_details_dto):

    # Arrange
    title = "title_1"
    description = "description_1"
    project = 1
    state = 2
    user_id = 1
    issue_type = "Bug"

    storage = TaskStorageImplementation()

    # Act
    response = storage.create_task(title=title,
                                  description=description,
                                  project=project,
                                  state=state,
                                  user_id=user_id,
                                  issue_type=issue_type)

    # Assert
    assert task_details_dto == response