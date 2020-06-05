import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from project_management_portal.constants.exception_messages import \
    INVALID_PROJECT
from project_management_portal.presenters.presenter_implementation import \
    PresenterImplementation


def test_is_valid_project_id():

    # Arrange
    presenter = PresenterImplementation()
    exception_message = INVALID_PROJECT[0]
    exception_res_status = INVALID_PROJECT[1]

    # Act
    with pytest.raises(NotFound) as exception:
        presenter.raise_invalid_project_id_exception()

    # Assert
    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_res_status
