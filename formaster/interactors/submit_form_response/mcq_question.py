from formaster.interactors.storages.storage_interface import StorageInterface
from formaster.interactors.submit_form_response.base import BaseSubmitFormResponseInteractor
from formaster.exceptions.exceptions import InvalidUserResponseSubmitException


class MCQQuestionSubmitFormResponseInteractor(
    BaseSubmitFormResponseInteractor):

    def __init__(self, storage: StorageInterface, question_id: int,
                 form_id: int, user_id: int, user_submitted_option_id: int):
        super().__init__(storage, question_id, form_id, user_id)
        self.user_submitted_option_id = user_submitted_option_id

    def _validate_user_response(self):
        option_ids = self.storage.get_option_ids_for_question(
            question_id=self.question_id
        )
        is_valid_option_id = self.user_submitted_option_id not in option_ids

        if is_valid_option_id:
            raise InvalidUserResponseSubmitException(
                self.user_submitted_option_id
            )

    def _create_user_response(self):
        response_id = self.storage.create_user_mcq_response(
            self.user_id, self.question_id, self.user_submitted_option_id
        )
        return response_id
