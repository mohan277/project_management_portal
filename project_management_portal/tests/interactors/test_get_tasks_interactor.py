import pytest
import datetime
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound
from project_management_portal.interactors.get_tasks_interactor import \
    GetTasksInteractor
from project_management_portal.interactors.storages. \
    task_storage_interface import TaskStorageInterface
from project_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface
from project_management_portal.interactors.storages.dtos import \
    ListOfTasksDto


def test_get_tasks_with_invalid_project_id_raises_exception():

    # Arrange
    project_id = 1
    storage = create_autospec(TaskStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = GetTasksInteractor(
        storage=storage,
        presenter=presenter
    )

    storage.is_valid_project_id.return_value = False
    presenter.raise_invalid_project_id_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.get_list_of_tasks(project_id=project_id)

    # Assert
    storage.is_valid_project_id.assert_called_once_with(project=project_id)
    presenter.raise_invalid_project_id_exception.assert_called_once()


def test_get_tasks_returns_list_of_tasks(list_of_task_dtos,
                                         get_tasks_expected_output):

    # Arrange
    project_id = 1
    storage = create_autospec(TaskStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = GetTasksInteractor(
        storage=storage,
        presenter=presenter
    )

    list_of_tasks_dto = ListOfTasksDto(
        list_of_task_dtos=list_of_task_dtos,
        total_count_of_tasks=1
    )

    storage.is_valid_project_id.return_value = True
    storage.get_list_of_tasks.return_value = list_of_tasks_dto
    presenter.get_list_of_tasks_response.return_value = get_tasks_expected_output

    # Act
    response = interactor.get_list_of_tasks(project_id=project_id)

    # Assert
    storage.get_list_of_tasks.assert_called_once_with(project_id=project_id)

    presenter.get_list_of_tasks_response.assert_called_once_with(
        list_of_tasks_dto=list_of_tasks_dto
    )

    assert response == get_tasks_expected_output
