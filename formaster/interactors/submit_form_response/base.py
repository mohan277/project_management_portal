from abc import abstractmethod
from formaster.interactors.mixins.form_validation import FormValidationMixin
from formaster.interactors.storages.storage_interface import StorageInterface
from formaster.interactors.presenters.presenter_interface import \
    PresenterInterface
from formaster.exceptions.exceptions import (
    FormClosedException,
    FormDoesNotExistException,
    QuestionDoesNotBelongToForm,
    InvalidUserResponseSubmitException
)


class BaseSubmitFormResponseInteractor(FormValidationMixin):

    def __init__(self, storage: StorageInterface,
                 user_id: int, form_id: int, question_id: int):

        self.user_id = user_id
        self.form_id = form_id
        self.question_id = question_id
        self.storage = storage

    def submit_form_response_wrapper(self, presenter: PresenterInterface):
        try:
            user_response_id = self.submit_form_response()
            response = presenter.submit_form_response_details(
                user_response_id=user_response_id
            )
            return response
        except FormClosedException as err:
            raise presenter.raise_form_closed_exception(err)
        except FormDoesNotExistException as err:
            raise presenter.raise_invalid_form_id(err)
        except QuestionDoesNotBelongToForm as err:
            raise presenter.raise_question_does_not_belong_to_form_exception(
                err
            )
        except InvalidUserResponseSubmitException as err:
            raise presenter.raise_invalid_user_response_submitted_exception(
                err
            )

    def submit_form_response(self):
        self.validate_form_is_live(form_id=self.form_id)
        self.storage.validate_question_id_with_form(
            question_id=self.question_id, form_id=self.form_id)
        self.storage.validate_form(form_id=self.form_id)
        self._validate_user_response()
        user_response_id = self._create_user_response()
        return user_response_id

    @abstractmethod
    def _validate_user_response(self):
        pass

    @abstractmethod
    def _create_user_response(self):
        pass
