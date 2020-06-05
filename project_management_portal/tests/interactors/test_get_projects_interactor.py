import pytest
import datetime
from django_swagger_utils.drf_server.exceptions import BadRequest
from unittest.mock import create_autospec
from project_management_portal.interactors.get_projects_interactor import \
    GetProjectsInteractor
from project_management_portal.interactors.storages. \
    project_storage_interface import ProjectStorageInterface
from project_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface
from project_management_portal.interactors.storages.dtos import ListOfProjectsDto


def test_get_projects_with_invalid_limit_value_raises_exception():

    # Arrange
    limit = 10
    offset = 0
    user_id = 1
    storage = create_autospec(ProjectStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = GetProjectsInteractor(
        storage=storage,
        presenter=presenter
    )

    storage.is_valid_limit.return_value = False
    presenter.raise_invalid_limit_value_exception.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.get_list_of_projects(limit=limit,
                                        offset=offset,
                                        user_id=user_id)

    # Assert
    storage.is_valid_limit.assert_called_once_with(limit=limit)
    presenter.raise_invalid_limit_value_exception.assert_called_once()


def test_get_projects_with_invalid_offset_value_raises_exception():

    # Arrange
    limit = 10
    offset = 0
    user_id = 1
    storage = create_autospec(ProjectStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = GetProjectsInteractor(
        storage=storage,
        presenter=presenter
    )

    storage.is_valid_offset.return_value = False
    presenter.raise_invalid_offset_value_exception.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.get_list_of_projects(limit=limit,
                                        offset=offset,
                                        user_id=user_id)

    # Assert
    storage.is_valid_offset.assert_called_once_with(offset=offset)
    presenter.raise_invalid_offset_value_exception.assert_called_once()


def test_get_projects_returns_list_of_admin_projects(project_details_dto,
                                               get_projects_expected_output):

    # Arrange
    limit = 10
    offset = 0
    user_id = 1
    total_count_of_projects = 1
    storage = create_autospec(ProjectStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = GetProjectsInteractor(
        storage=storage,
        presenter=presenter
    )

    list_of_project_dtos = ListOfProjectsDto(
        list_of_project_dtos=project_details_dto,
        total_count_of_projects=total_count_of_projects
    )

    storage.is_admin.return_value = True
    storage.get_list_of_admin_projects.return_value = list_of_project_dtos
    presenter.get_list_of_projects_response. \
        return_value = get_projects_expected_output

    # Act
    response = interactor.get_list_of_projects(
        limit=limit, offset=offset, user_id=user_id)

    # Assert
    storage.get_list_of_admin_projects.assert_called_once_with(
        limit=limit, offset=offset, user_id=user_id)

    presenter.get_list_of_projects_response.assert_called_once_with(
        list_of_projects_dto=list_of_project_dtos
    )

    assert response == get_projects_expected_output


def test_get_projects_returns_list_of_member_projects(project_details_dto,
                                               get_projects_expected_output):

    # Arrange
    limit = 10
    offset = 0
    user_id = 2
    total_count_of_projects = 1
    storage = create_autospec(ProjectStorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = GetProjectsInteractor(
        storage=storage,
        presenter=presenter
    )

    list_of_project_dtos = ListOfProjectsDto(
        list_of_project_dtos=project_details_dto,
        total_count_of_projects=total_count_of_projects
    )

    storage.is_admin.return_value = False
    storage.get_list_of_member_projects.return_value = list_of_project_dtos
    presenter.get_list_of_projects_response. \
        return_value = get_projects_expected_output

    # Act
    response = interactor.get_list_of_projects(
        limit=limit, offset=offset, user_id=user_id)

    # Assert
    storage.get_list_of_member_projects.assert_called_once_with(
        limit=limit, offset=offset, user_id=user_id)

    presenter.get_list_of_projects_response.assert_called_once_with(
        list_of_projects_dto=list_of_project_dtos
    )

    assert response == get_projects_expected_output
