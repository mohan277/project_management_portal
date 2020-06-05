from project_management_portal.models import State, Project, Transition, Task
from project_management_portal.interactors.storages. \
    transition_storage_interface import TransitionStorageInterface
from project_management_portal.interactors.storages.dtos import (
    ToStateDto,
    FromStateDto,
    TransitionDto
)


class TransitionStorageImplementation(TransitionStorageInterface):

    def create_transition(self,
                          name: str,
                          description: str,
                          from_state: int,
                          to_state: int):

        from_state_obj = State.objects.get(id=from_state)

        to_state_obj = State.objects.get(id=to_state)

        from_state_dto = self._get_from_state_dto(from_state_obj)

        to_state_dto = self._get_to_state_dto(to_state_obj)

        transition_obj = Transition.objects.create(name=name,
                                                   description=description,
                                                   from_state_id=from_state,
                                                   to_state_id=to_state)

        transition_details_dto = self._get_transition_details_dto(
            transition_obj, from_state_dto, to_state_dto)

        return transition_details_dto


    def _get_from_state_dto(self, from_state_obj):

        from_state_dto = FromStateDto(
            name=from_state_obj.name,
            from_state_id=from_state_obj.id
        )

        return from_state_dto


    def _get_to_state_dto(self, to_state_obj):

        to_state_dto = ToStateDto(
            name=to_state_obj.name,
            to_state_id=to_state_obj.id
        )

        return to_state_dto


    def _get_transition_details_dto(self,
                                    transition_obj,
                                    from_state_dto,to_state_dto):

        transition_details_dto = TransitionDto(
            name=transition_obj.name,
            transition_id=transition_obj.id,
            description=transition_obj.description,
            from_state=from_state_dto,
            to_state=to_state_dto
        )

        return transition_details_dto


    def is_valid_from_state_id(self, from_state: int):

        is_from_state_id_valid = State.objects. \
            filter(id=from_state).exists()

        return is_from_state_id_valid


    def is_valid_to_state_id(self, to_state: int):

        is_to_state_id_valid = State.objects. \
            filter(id=to_state).exists()

        return is_to_state_id_valid


    def get_transition_details_between_two_states(self,
                                                  task_id: int,
                                                  project_id: int,
                                                  to_state: int):


        task_obj = Task.objects.get(id=task_id)



        transition
        # from_state = Transition.objects.filter(
        #     workflows__projects__tasks__id=task_id,
        #     workflows__projects__id=project_id,
        #     to_state_id=to_state)
        # t - p - w - t
