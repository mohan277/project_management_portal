import pytest
import datetime
from project_management_portal.presenters.presenter_implementation import \
    PresenterImplementation


def test_get_tasks_returns_list_of_tasks(
    list_of_tasks_dto, get_tasks_expected_output):

    # Arrange
    presenter = PresenterImplementation()

    # Act
    response = presenter.get_list_of_tasks_response(
        list_of_tasks_dto=list_of_tasks_dto
    )

    # Assert
    assert response == get_tasks_expected_output
