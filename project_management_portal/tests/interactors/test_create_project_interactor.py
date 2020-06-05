import pytest
from unittest .mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound
from project_management_portal.interactors.storages. \
    project_storage_interface import ProjectStorageInterface
from project_management_portal.interactors.create_project_interactor \
    import CreateProjectInteractor
from project_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface


def test_create_project_with_invalid_workflow_type_id_and_users_list_raises_exception():

    # Arrange
    user_id = 1
    assigned_to = [1, 2, 3]
    name = "project_management_portal"
    description = "The name of the project is Project Management Portal"
    workflow_type = 1
    project_type = "CRM"

    storage = create_autospec(ProjectStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = CreateProjectInteractor(
        storage=storage,
        presenter=presenter
    )


    storage.is_valid_workflow_type_id.return_value = False
    presenter.raise_invalid_workflow_type_id_exception.side_effect = NotFound

    interactor = CreateProjectInteractor(
        storage=storage,
        presenter=presenter
    )

    # Act
    with pytest.raises(NotFound):
        interactor.create_project(
            user_id=user_id,
            assigned_to=assigned_to,
            name=name,
            description=description,
            workflow_type=workflow_type,
            project_type=project_type
        )

    # Assert
    storage.is_valid_workflow_type_id.assert_called_once_with(
        workflow_type=workflow_type
    )
    presenter.raise_invalid_workflow_type_id_exception.assert_called_once()


def test_create_project_with_invalid_workflow_type_id_raises_exception():

    # Arrange
    user_id = 1
    assigned_to = [1, 2, 3]
    name = "project_management_portal"
    description = "The name of the project is Project Management Portal"
    workflow_type = 1
    project_type = "CRM"

    storage = create_autospec(ProjectStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = CreateProjectInteractor(
        storage=storage,
        presenter=presenter
    )


    storage.is_valid_workflow_type_id.return_value = False
    presenter.raise_invalid_workflow_type_id_exception.side_effect = NotFound

    interactor = CreateProjectInteractor(
        storage=storage,
        presenter=presenter
    )

    # Act
    with pytest.raises(NotFound):
        interactor.create_project(
            user_id=user_id,
            assigned_to=assigned_to,
            name=name,
            description=description,
            workflow_type=workflow_type,
            project_type=project_type
        )

    # Assert
    storage.is_valid_workflow_type_id.assert_called_once_with(
        workflow_type=workflow_type
    )
    presenter.raise_invalid_workflow_type_id_exception.assert_called_once()


def test_create_project_with_invalid_admin_raises_exception():

    # Arrange
    user_id = 1
    assigned_to = [1, 2, 3]
    name = "project_management_portal"
    description = "The name of the project is Project Management Portal"
    workflow_type = 1
    project_type = "CRM"

    storage = create_autospec(ProjectStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = CreateProjectInteractor(
        storage=storage,
        presenter=presenter
    )


    storage.is_admin.return_value = False
    presenter.raise_invalid_admin_exception.side_effect = NotFound

    interactor = CreateProjectInteractor(
        storage=storage,
        presenter=presenter
    )

    # Act
    with pytest.raises(NotFound):
        interactor.create_project(
            user_id=user_id,
            assigned_to=assigned_to,
            name=name,
            description=description,
            workflow_type=workflow_type,
            project_type=project_type
        )

    # Assert
    storage.is_admin.assert_called_once_with(user_id=user_id)
    presenter.raise_invalid_admin_exception.assert_called_once()


def test_create_project_with_invalid_list_of_user_ids_raises_exception():

    # Arrange
    user_id = 1
    assigned_to = [1, 2, 3]
    name = "project_management_portal"
    description = "The name of the project is Project Management Portal"
    workflow_type = 1
    project_type = "CRM"

    storage = create_autospec(ProjectStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = CreateProjectInteractor(
        storage=storage,
        presenter=presenter
    )

    storage.is_valid_user_ids_list.return_value = False
    presenter.raise_invalid_list_of_user_ids_exception.side_effect = NotFound

    interactor = CreateProjectInteractor(
        storage=storage,
        presenter=presenter
    )

    # Act
    with pytest.raises(NotFound):
        interactor.create_project(
            user_id=user_id,
            assigned_to=assigned_to,
            name=name,
            description=description,
            workflow_type=workflow_type,
            project_type=project_type
        )

    # Assert
    storage.is_valid_user_ids_list.assert_called_once_with(
        assigned_to=assigned_to
    )
    presenter.raise_invalid_list_of_user_ids_exception.assert_called_once()


def test_create_project_with_valid_details_returns_project_details(
    project_details_dto, create_project_expected_output):

    # Arrange
    user_id = 1
    assigned_to = [1, 2, 3]
    name = "project_management_portal"
    description = "The name of the project is Project Management Portal"
    workflow_type = 1
    project_type = "CRM"

    storage = create_autospec(ProjectStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = CreateProjectInteractor(
        storage=storage,
        presenter=presenter
    )

    storage.is_valid_workflow_type_id.return_value = True
    storage.is_valid_user_ids_list.return_value = True
    storage.create_project.return_value = project_details_dto
    presenter.get_create_project_response. \
        return_value = create_project_expected_output

    # Act
    response = interactor.create_project(
        name=name,
        user_id=user_id,
        assigned_to=assigned_to,
        description=description,
        workflow_type=workflow_type,
        project_type=project_type
    )

    # Assert
    storage.create_project.assert_called_once_with(
        name=name,
        user_id=user_id,
        assigned_to=assigned_to,
        description=description,
        workflow_type=workflow_type,
        project_type=project_type
    )

    presenter.get_create_project_response.assert_called_once_with(
        project_details_dto=project_details_dto
    )

    assert response == create_project_expected_output
