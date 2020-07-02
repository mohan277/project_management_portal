import pytest
import datetime
from django_swagger_utils.drf_server.exceptions import BadRequest
from unittest.mock import create_autospec, patch
from project_management_portal.interactors.get_projects_interactor import \
    GetProjectsInteractor
from project_management_portal.interactors.storages. \
    project_storage_interface import ProjectStorageInterface
from project_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface
from project_management_portal.interactors.storages.dtos import \
    IsAdminDTO, ListOfProjectsDto, FinalProjectDTO


def test_get_projects_with_invalid_limit_value_raises_exception():

    # Arrange
    limit = -1
    offset = 0
    user_id = 1
    storage = create_autospec(ProjectStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetProjectsInteractor(storage=storage)

    presenter.raise_invalid_limit_value_exception.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.get_list_of_projects_wrapper(limit=limit,
                                                offset=offset,
                                                user_id=user_id,
                                                presenter=presenter)

    # Assert
    presenter.raise_invalid_limit_value_exception.assert_called_once()


def test_get_projects_with_invalid_offset_value_raises_exception():

    # Arrange
    limit = 10
    offset = -1
    user_id = 1
    storage = create_autospec(ProjectStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetProjectsInteractor(storage=storage)

    presenter.raise_invalid_offset_value_exception.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.get_list_of_projects_wrapper(limit=limit,
                                                offset=offset,
                                                user_id=user_id,
                                                presenter=presenter)

    # Assert
    presenter.raise_invalid_offset_value_exception.assert_called_once()


@patch(
    'project_management_portal_auth.interfaces.service_interface.ServiceInterface.get_user_dtos')
@patch(
    'project_management_portal_auth.interfaces.service_interface.ServiceInterface.get_is_admin_valid_dto')
def test_get_projects_returns_list_of_admin_projects(
    get_is_admin_valid_dto,
    get_user_dtos,
    list_of_project_details_dtos,
    user_details_dtos,
    get_projects_expected_output,
    final_list_of_projects_details_dto):

    # Arrange
    limit = 10
    offset = 0
    user_id = 1
    total_count_of_projects = 2
    is_admin_valid_dto = IsAdminDTO(is_admin=True)

    storage = create_autospec(ProjectStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetProjectsInteractor(storage=storage)

    get_is_admin_valid_dto.return_value = is_admin_valid_dto
    get_user_dtos.return_value = user_details_dtos
    storage.get_list_of_admin_projects.return_value = list_of_project_details_dtos
    presenter.get_list_of_projects_response. \
        return_value = get_projects_expected_output

    # Act
    response = interactor.get_list_of_projects_wrapper(limit=limit,
                                                       offset=offset,
                                                       user_id=user_id,
                                                       presenter=presenter)

    # Assert
    storage.get_list_of_admin_projects.assert_called_once_with(
        limit=limit, offset=offset, user_id=user_id)

    presenter.get_list_of_projects_response.assert_called_once_with(
        list_of_projects_dto=list_of_project_details_dtos
    )
    get_is_admin_valid_dto.assert_called_once_with(user_id=user_id)
    # get_user_dtos.assert_called_once_with(user_ids=user_ids)
    assert response == get_projects_expected_output


# def test_get_projects_returns_list_of_member_projects(project_details_dto,
#                                               get_projects_expected_output):

#     # Arrange
#     limit = 10
#     offset = 0
#     user_id = 2
#     total_count_of_projects = 1
#     storage = create_autospec(ProjectStorageInterface)
#     presenter = create_autospec(PresenterInterface)

#     interactor = GetProjectsInteractor(
#         storage=storage,
#         presenter=presenter
#     )

#     list_of_project_dtos = ListOfProjectsDto(
#         list_of_project_dtos=project_details_dto,
#         total_count_of_projects=total_count_of_projects
#     )

#     storage.is_admin.return_value = False
#     storage.get_list_of_member_projects.return_value = list_of_project_dtos
#     presenter.get_list_of_projects_response. \
#         return_value = get_projects_expected_output

#     # Act
#     response = interactor.get_list_of_projects(
#         limit=limit, offset=offset, user_id=user_id)

#     # Assert
#     storage.get_list_of_member_projects.assert_called_once_with(
#         limit=limit, offset=offset, user_id=user_id)

#     presenter.get_list_of_projects_response.assert_called_once_with(
#         list_of_projects_dto=list_of_project_dtos
#     )

#     assert response == get_projects_expected_output
