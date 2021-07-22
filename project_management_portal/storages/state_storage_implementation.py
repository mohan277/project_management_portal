from typing import List
from project_management_portal.models import Project, Workflow, Task, \
    Transition
from project_management_portal.interactors.storages. \
    state_storage_interface import StateStorageInterface
from project_management_portal.exceptions import \
    InvalidTaskIdException
from project_management_portal.interactors.storages.dtos import \
    ToStateDto, ListOfToStatesDto


class StateStorageImplementation(StateStorageInterface):

    def is_valid_task_id(self, task_id: int):

        is_task_id_valid = Task.objects. \
            filter(id=task_id).exists()

        return is_task_id_valid


    def get_to_states_based_on_current_state(self, task_id: int):

        current_state_id = Task.objects.get(id=task_id).state_id

        transition_objs = Transition.objects.filter(
            workflows__projects__tasks__id=task_id,
            from_state_id=current_state_id)

        total_count_of_to_states = len(transition_objs)

        list_of_to_state_dtos = []

        for transition_obj in transition_objs:

            list_of_to_state_dtos.append(
                self._get_to_state_details_dto(transition_obj))

        list_of_to_states_dto = ListOfToStatesDto(
            list_of_to_state_dtos=list_of_to_state_dtos,
            total_count_of_to_states=total_count_of_to_states)

        return list_of_to_states_dto

    @staticmethod
    def _get_to_state_details_dto(transition_obj):

        to_state_dto = ToStateDto(
            name=transition_obj.to_state.name,
            to_state_id=transition_obj.to_state_id)

        return to_state_dto
