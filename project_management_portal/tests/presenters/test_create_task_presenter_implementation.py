import pytest
import datetime
from project_management_portal.presenters.presenter_implementation import \
    PresenterImplementation


def test_create_task_valid_details_returns_created_task_details(
    task_details_dto, create_task_expected_output):

    # Arrange
    presenter = PresenterImplementation()

    # Act
    response = presenter.get_create_task_response(
        task_details_dto=task_details_dto
    )

    # Assert
    assert response == create_task_expected_output
