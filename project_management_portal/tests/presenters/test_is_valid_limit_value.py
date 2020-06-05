import pytest
from django_swagger_utils.drf_server.exceptions import BadRequest
from project_management_portal.constants.exception_messages import \
    INVALID_LIMIT_VALUE
from project_management_portal.presenters.presenter_implementation import \
    PresenterImplementation


def test_is_valid_workflow_type():

    # Arrange
    presenter = PresenterImplementation()
    exception_message = INVALID_LIMIT_VALUE[0]
    exception_res_status = INVALID_LIMIT_VALUE[1]

    # Act
    with pytest.raises(BadRequest) as exception:
        presenter.raise_invalid_limit_value_exception()

    # Assert
    assert exception.value.message == exception_message
    assert exception.value.res_status == exception_res_status
