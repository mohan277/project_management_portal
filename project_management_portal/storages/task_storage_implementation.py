from typing import List
from project_management_portal.models import Task, Project, State, User
from project_management_portal.interactors.storages. \
    task_storage_interface import TaskStorageInterface
from project_management_portal.exceptions import \
    InvalidProjectIdException, InvalidListOfUserIdsException
from project_management_portal.interactors.storages.dtos import (
    TaskDto,
    StateDto,
    TaskProjectDto,
    ListOfTasksDto
)


class TaskStorageImplementation(TaskStorageInterface):

    def create_task(self,
                    title: str,
                    user_id: int,
                    description: str,
                    project: int,
                    state: int,
                    issue_type: str):

        task_obj = Task.objects.create(title=title,
                                       project_id=project,
                                       state_id=state,
                                       created_by_id=user_id,
                                       description=description,
                                       issue_type=issue_type)

        task_details_dto = self._get_task_details_dto(task_obj)

        return task_details_dto


    def get_list_of_tasks(self, project_id) -> ListOfTasksDto:

        list_of_task_objs = Task.objects.filter(project=project_id)

        total_count_of_tasks = len(list_of_task_objs)

        list_of_task_dtos = self._get_list_of_task_dtos(
            list_of_task_objs
        )

        list_of_tasks_dto = ListOfTasksDto(
            list_of_task_dtos=list_of_task_dtos,
            total_count_of_tasks=total_count_of_tasks
        )

        return list_of_tasks_dto


    def _get_list_of_task_dtos(self, task_objs):

            list_of_task_dtos = []

            for task_obj in task_objs:
                list_of_task_dtos.append(self._get_task_details_dto(task_obj))

            return list_of_task_dtos


    def _get_task_details_dto(self, task_obj):

        task_details_dto = TaskDto(
            task_id=task_obj.id,
            title=task_obj.title,
            description=task_obj.description,
            project=task_obj.project.name,
            state=task_obj.state.name,
            created_by=task_obj.created_by.username,
            created_at=task_obj.created_at,
            issue_type=task_obj.issue_type
        )

        return task_details_dto


    def is_valid_project_id(self, project: int):

        is_project_id_valid = Project.objects.filter(id=project).exists()
        print(is_project_id_valid)

        return is_project_id_valid


    def is_valid_state_id(self, state: int):

        is_state_id_valid = State.objects.filter(id=state).exists()

        return is_state_id_valid


    def is_valid_user_id(self, user_id: int):

        is_user_id_valid = User.objects.filter(id=user_id).exists()

        return is_user_id_valid
