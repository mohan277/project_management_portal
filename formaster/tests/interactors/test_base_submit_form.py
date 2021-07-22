import pytest
from unittest.mock import create_autospec
from formaster.interactors.storages.dtos import FormDto
from django_swagger_utils.drf_server.exceptions import NotFound, Forbidden
from formaster.interactors.submit_form_response.base import \
    BaseSubmitFormResponseInteractor
from formaster.interactors.storages.storage_interface import StorageInterface
from formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from formaster.exceptions.exceptions import(
    FormDoesNotExistException,
    QuestionDoesNotBelongToForm,
    FormClosedException
)


def test_base_submit_form_with_invalid_form_id_raises_exception():

    # Arrange
    user_id = 1
    form_id = 1
    question_id = 1
    err = FormDoesNotExistException(form_id)
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = BaseSubmitFormResponseInteractor(
        storage=storage,
        user_id=user_id,
        form_id=form_id,
        question_id=question_id
    )
    storage.validate_form.side_effect = err
    presenter.raise_invalid_form_id.side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.submit_form_response_wrapper(presenter=presenter)

    # Assert
    storage.validate_form.assert_called_once_with(form_id=form_id)
    presenter.raise_invalid_form_id.assert_called_once_with(err)


def test_base_submit_form_with_invalid_question_id_with_form_raises_exception():

    # Arrange
    user_id = 1
    form_id = 1
    question_id = 1
    err = QuestionDoesNotBelongToForm(question_id)
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = BaseSubmitFormResponseInteractor(
        storage=storage,
        user_id=user_id,
        form_id=form_id,
        question_id=question_id
    )
    storage.validate_question_id_with_form.side_effect = err
    presenter.raise_question_does_not_belong_to_form_exception. \
        side_effect = NotFound

    # Act
    with pytest.raises(NotFound):
        interactor.submit_form_response_wrapper(presenter=presenter)

    # Assert
    storage.validate_question_id_with_form.assert_called_once_with(
        question_id=question_id,
        form_id=form_id
    )
    presenter.raise_question_does_not_belong_to_form_exception. \
        assert_called_once_with(err)


def test_base_submit_form_when_form_id_is_not_live_raises_exception():

    # Arrange
    user_id = 1
    form_id = 1
    question_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = BaseSubmitFormResponseInteractor(
        storage=storage,
        user_id=user_id,
        form_id=form_id,
        question_id=question_id
    )
    form_dto = FormDto(
        is_live=False
    )

    storage.get_form_dto.return_value = form_dto
    presenter.raise_form_closed_exception.side_effect = Forbidden
    # Act
    with pytest.raises(Forbidden):
        interactor.submit_form_response_wrapper(presenter=presenter)

    # Assert
    call_args = presenter.raise_form_closed_exception.call_args
    assert call_args.args[0].args[0] == form_id
