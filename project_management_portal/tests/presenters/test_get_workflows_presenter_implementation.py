import pytest
import datetime
from project_management_portal.interactors.storages.dtos import \
    ProjectDto, UserDto, WorkflowTypeDto
from project_management_portal.presenters.presenter_implementation import \
    PresenterImplementation


def test_get_workflows_returns_list_of_workflows(
    get_workflows_expected_output_response, list_of_workflows_dto):

    # Arrange
    presenter = PresenterImplementation()

    # Act
    response = presenter.get_list_of_workflows_response(
        list_of_workflows_dto=list_of_workflows_dto
    )

    # Assert
    assert response == get_workflows_expected_output_response
