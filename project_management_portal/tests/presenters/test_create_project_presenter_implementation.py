import pytest
import datetime
from project_management_portal.presenters.presenter_implementation import \
    PresenterImplementation


def test_create_project_valid_details_returns_created_project_details(
    project_details_dto,
    create_project_expected_output_response):

    # Arrange
    presenter = PresenterImplementation()

    # Act
    response = presenter.get_create_project_response(
        project_details_dto=project_details_dto
    )

    # Assert
    assert response == create_project_expected_output_response
