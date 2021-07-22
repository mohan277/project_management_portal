import pytest
import datetime
from project_management_portal.interactors.storages.dtos import \
    ProjectDto, UserDto, WorkflowTypeDto
from project_management_portal.presenters.presenter_implementation import \
    PresenterImplementation


def test_get_admin_projects_returns_list_of_projects(
    list_of_projects_dto, get_admin_projects_expected_output_response):

    # Arrange
    presenter = PresenterImplementation()

    # Act
    response = presenter.get_list_of_projects_response(
        list_of_projects_dto=list_of_projects_dto
    )

    # Assert
    assert response == get_admin_projects_expected_output_response
