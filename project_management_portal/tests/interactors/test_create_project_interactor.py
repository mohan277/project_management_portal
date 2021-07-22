import pytest
from project_management_portal.interactors.storages.dtos import IsAdminDTO
from unittest.mock import create_autospec, patch
from django_swagger_utils.drf_server.exceptions import NotFound
from project_management_portal.interactors.storages. \
    project_storage_interface import ProjectStorageInterface
from project_management_portal.interactors.create_project_interactor \
    import CreateProjectInteractor
from project_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface


def test_create_project_with_invalid_workflow_type_id_raises_exception():

    # Arrange
    user_id = 1
    developers = [1, 2]
    name = "project_management_portal"
    description = "The name of the project is Project Management Portal"
    workflow_type = 1
    project_type = "CRM"

    storage = create_autospec(ProjectStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = CreateProjectInteractor(storage=storage)

    storage.is_valid_workflow_type_id.return_value = False
    presenter.raise_invalid_workflow_type_id_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_project_wrapper(
            name=name,
            user_id=user_id,
            presenter=presenter,
            developers=developers,
            description=description,
            project_type=project_type,
            workflow_type=workflow_type
        )

    # Assert
    storage.is_valid_workflow_type_id.assert_called_once_with(
        workflow_type=workflow_type
    )
    presenter.raise_invalid_workflow_type_id_exception.assert_called_once()


@patch(
    'project_management_portal_auth.interfaces.service_interface.ServiceInterface.get_is_admin_valid_dto')
def test_with_invalid_admin_raises_exception(get_is_admin_valid_dto):

    # Arrange
    user_id = 1
    developers = [1, 2]
    name = "project_management_portal"
    description = "The name of the project is Project Management Portal"
    workflow_type = 1
    project_type = "CRM"
    is_admin_valid_dto = IsAdminDTO(is_admin=False)

    storage = create_autospec(ProjectStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = CreateProjectInteractor(storage=storage)

    is_admin_valid_dto = IsAdminDTO(is_admin=False)
    get_is_admin_valid_dto.return_value = is_admin_valid_dto
    presenter.raise_invalid_admin_exception.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.create_project_wrapper(
            name=name,
            user_id=user_id,
            presenter=presenter,
            developers=developers,
            description=description,
            project_type=project_type,
            workflow_type=workflow_type
        )

    # Assert
    get_is_admin_valid_dto.assert_called_once_with(user_id=user_id)
    presenter.raise_invalid_admin_exception.assert_called_once()


@patch(
    'project_management_portal_auth.interfaces.service_interface.ServiceInterface.get_user_dtos')
@patch(
    'project_management_portal_auth.interfaces.service_interface.ServiceInterface.get_is_admin_valid_dto')
def test_create_project_with_valid_details_returns_project_details(
    get_is_admin_valid_dto, get_user_dtos, final_project_details_dto, user_details_dtos, \
        project_details_dto, create_project_expected_output):

    # Arrange
    user_id = 1
    developers = [1, 2]
    name = "project_management_portal"
    description = "The name of the project is Project Management Portal"
    workflow_type = 1
    project_type = "CRM"
    is_admin_valid_dto = IsAdminDTO(is_admin=True)

    storage = create_autospec(ProjectStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = CreateProjectInteractor(storage=storage)

    get_is_admin_valid_dto.return_value = is_admin_valid_dto
    get_user_dtos.return_value = user_details_dtos
    storage.is_valid_workflow_type_id.return_value = True
    storage.create_project.return_value = project_details_dto
    presenter.get_create_project_response. \
        return_value = create_project_expected_output

    # Act
    response = interactor.create_project_wrapper(
        name=name,
        user_id=user_id,
        presenter=presenter,
        developers=developers,
        description=description,
        project_type=project_type,
        workflow_type=workflow_type
    )

    # Assert
    get_is_admin_valid_dto.assert_called_once_with(user_id=user_id)
    get_user_dtos.assert_called_once_with(user_ids=developers)
    storage.create_project.assert_called_once_with(
        name=name,
        user_id=user_id,
        developers=developers,
        description=description,
        project_type=project_type,
        workflow_type=workflow_type
    )

    presenter.get_create_project_response.assert_called_once_with(
        project_details_dto=final_project_details_dto
    )

    assert response == create_project_expected_output
