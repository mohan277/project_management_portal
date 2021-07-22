import pytest
from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import NotFound
from formaster.interactors.submit_form_response.mcq_question import \
    MCQQuestionSubmitFormResponseInteractor
from formaster.interactors.storages.storage_interface import StorageInterface
from formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from formaster.exceptions.exceptions import InvalidUserResponseSubmitException


def test_mcq_question_with_invalid_user_submitted_option_id_raises_exception():

    # Arrange
    user_id = 1
    form_id = 1
    question_id = 1
    user_submitted_option_id = 5
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = MCQQuestionSubmitFormResponseInteractor(
        storage=storage,
        user_id=user_id,
        form_id=form_id,
        question_id=question_id,
        user_submitted_option_id=user_submitted_option_id
    )
    storage.get_option_ids_for_question.return_value = [1, 2, 3, 4]
    presenter.raise_invalid_user_response_submitted_exception. \
        side_effect = NotFound
    # Act
    with pytest.raises(NotFound):
        interactor.submit_form_response_wrapper(presenter=presenter)

    # Assert
    call_args = presenter.raise_invalid_user_response_submitted_exception. \
        call_args
    assert call_args.args[0].args[0] == user_submitted_option_id


def test_mcq_question_with_valid_details_returns_exception():

    # Arrange
    user_id = 1
    form_id = 1
    question_id = 1
    user_response_id = 1
    user_submitted_option_id = 1
    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)

    interactor = MCQQuestionSubmitFormResponseInteractor(
        storage=storage,
        user_id=user_id,
        form_id=form_id,
        question_id=question_id,
        user_submitted_option_id=user_submitted_option_id
    )
    storage.get_option_ids_for_question.return_value = [1, 2, 3, 4]
    storage.create_user_mcq_response.return_value = user_response_id
    presenter.submit_form_response_details.return_value = user_response_id

    # Act
    response = interactor.submit_form_response_wrapper(presenter=presenter)

    # Assert
    storage.get_option_ids_for_question.assert_called_once_with(
        question_id=question_id
    )
    storage.create_user_mcq_response.assert_called_once_with(
        user_id=user_id,
        question_id=question_id,
        user_submitted_option_id=user_submitted_option_id
    )
    presenter.submit_form_response_details.assert_called_once_with(
        user_response_id=user_response_id
    )
    assert response == user_response_id
