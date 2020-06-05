import datetime
import pytest
from unittest .mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound
from project_management_portal.interactors.storages. \
    task_storage_interface import TaskStorageInterface
from project_management_portal.interactors.create_task_interactor \
    import CreateTaskInteractor
from project_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface


def test_create_task_with_invalid_project_id_raises_exception():

    # Arrange
    title = "title_1"
    description = "description"
    project = 10
    state = 1
    user_id = 1
    issue_type = "Bug"

    storage = create_autospec(TaskStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = CreateTaskInteractor(
        storage=storage,
        presenter=presenter
    )


    storage.is_valid_project_id.return_value = False
    presenter.raise_invalid_project_id_exception.side_effect = NotFound

    interactor = CreateTaskInteractor(
        storage=storage,
        presenter=presenter
    )

    # Act
    with pytest.raises(NotFound):
        interactor.create_task(
            title=title,
            user_id=user_id,
            description=description,
            project=project,
            state=state,
            issue_type=issue_type
        )

    # Assert
    storage.is_valid_project_id.assert_called_once_with(
        project=project
    )
    presenter.raise_invalid_project_id_exception.assert_called_once()


def test_create_task_with_invalid_state_id_raises_exception():

    # Arrange
    title = "title_1"
    description = "description"
    project = 1
    state = 10
    user_id = 1
    issue_type = "Bug"

    storage = create_autospec(TaskStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = CreateTaskInteractor(
        storage=storage,
        presenter=presenter
    )


    storage.is_valid_state_id.return_value = False
    presenter.raise_invalid_state_id_exception.side_effect = NotFound

    interactor = CreateTaskInteractor(
        storage=storage,
        presenter=presenter
    )

    # Act
    with pytest.raises(NotFound):
        interactor.create_task(
            title=title,
            user_id=user_id,
            description=description,
            project=project,
            state=state,
            issue_type=issue_type
        )

    # Assert
    storage.is_valid_state_id.assert_called_once_with(
        state=state
    )
    presenter.raise_invalid_state_id_exception.assert_called_once()


def test_create_task_with_invalid_user_id_raises_exception():

    # Arrange
    title = "title_1"
    description = "description"
    project = 1
    state = 10
    user_id = 1
    issue_type = "Bug"

    storage = create_autospec(TaskStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = CreateTaskInteractor(
        storage=storage,
        presenter=presenter
    )


    storage.is_valid_user_id.return_value = False
    presenter.raise_invalid_user_id_exception.side_effect = NotFound

    interactor = CreateTaskInteractor(
        storage=storage,
        presenter=presenter
    )

    # Act
    with pytest.raises(NotFound):
        interactor.create_task(
            title=title,
            user_id=user_id,
            description=description,
            project=project,
            state=state,
            issue_type=issue_type
        )

    # Assert
    storage.is_valid_user_id.assert_called_once_with(user_id=user_id)
    presenter.raise_invalid_user_id_exception.assert_called_once()


def test_create_task_with_valid_details_returns_task_details(
    task_details_dto, create_task_expected_output):

    # Arrange
    title = "title_1"
    description = "description"
    project = 1
    state = 1
    user_id = 1
    issue_type = "Bug"

    storage = create_autospec(TaskStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = CreateTaskInteractor(
        storage=storage,
        presenter=presenter
    )

    storage.create_task.return_value = task_details_dto
    presenter.get_create_task_response. \
        return_value = create_task_expected_output

    # Act
    response = interactor.create_task(
        title=title,
        user_id=user_id,
        description=description,
        project=project,
        state=state,
        issue_type=issue_type
    )

    # Assert
    storage.create_task.assert_called_once_with(
        title=title,
        user_id=user_id,
        description=description,
        project=project,
        state=state,
        issue_type=issue_type
    )

    presenter.get_create_task_response.assert_called_once_with(
        task_details_dto=task_details_dto
    )

    assert response == create_task_expected_output
