from abc import ABC
from abc import abstractmethod


class StorageInterface(ABC):

    @abstractmethod
    def get_form_dto(self, form_id: int):
        pass

    @abstractmethod
    def validate_question_id_with_form(self, question_id: int, form_id: int):
        pass

    @abstractmethod
    def validate_form(self, form_id: int):
        pass

    @abstractmethod
    def get_option_ids_for_question(self, question_id):
        pass

    @abstractmethod
    def create_user_mcq_response(self, user_id: int, question_id: int,
                                 user_submitted_option_id: int):
        pass
