import pytest
import datetime
from project_management_portal.presenters.presenter_implementation import \
    PresenterImplementation


def test_create_project_valid_details_returns_created_project_details(
    final_project_details_dto,
    create_project_expected_output_response):

    # Arrange
    presenter = PresenterImplementation()
    print("#"*100)
    print(final_project_details_dto)
    print("#"*100)
    # Act
    response = presenter.get_create_project_response(
        final_project_details_dto=final_project_details_dto
    )
    # Assert
    assert response == create_project_expected_output_response
