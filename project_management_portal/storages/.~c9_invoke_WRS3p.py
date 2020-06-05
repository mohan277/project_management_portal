from project_management_portal.models import Task, Project
from project_management_portal.interactors.storages. \
    task_storage_interface import TaskStorageInterface
from project_management_portal.exceptions import InvalidProjectIdException
from project_management_portal.interactors.storages.dtos import (
    WorkflowTypeDto,
    UserDto,
    ProjectDto,
    ListOfProjectsDto
)


class TaskStorageImplementation(TaskStorageInterface):


    def create_task(self,
                    name: str,
                    description: str,
                    project: int,
                    issue_type: str):

        project_obj = Project.objects.get(id=project)

        project_dto = self._get_project_dto(project_obj)


        task_obj = Task.objects.create(name=name,
                                       project_id=project,
                                       description=description,
                                       issue_type=issue_type)

        task_details_dto = self._get_task_details_dto(task_obj,
                                                      project_dto)

        return project_details_dto


    def get_list_of_projects(self, limit: int, offset: int) \
        -> ListOfProjectsDto:

        list_of_project_objs = Project.objects.prefetch_related(
            'user',
            'workflow_type')

        list_of_project_dtos = self._get_list_of_project_dtos(
            list_of_project_objs
        )

        final_list_of_project_dtos = list_of_project_dtos[offset:offset+limit]

        list_of_projects_dto = ListOfProjectsDto(
            projects_dto=final_list_of_project_dtos
        )

        return list_of_projects_dto


    def _get_list_of_project_dtos(self, project_objs):

            list_of_project_dtos = []

            for project_obj in project_objs:

                workflow_type_dto = self._get_workflow_type_dto(
                    project_obj.workflow_type
                )

                user_dto = self._get_user_dto(project_obj.user)

                project_dto = ProjectDto(
                    name=project_obj.name,
                    description=project_obj.description,
                    workflow_type=workflow_type_dto,
                    project_type=project_obj.project_type,
                    user=user_dto,
                    created_at=project_obj.created_at)

                list_of_project_dtos.append(project_dto)


            return list_of_project_dtos


    def _get_workflow_type_dto(self, workflow_type_obj):

        workflow_type_dto = WorkflowTypeDto(
            name=workflow_type_obj.name,
            workflow_type_id=workflow_type_obj.id
        )

        return workflow_type_dto

    def _get_user_dto(self, user_obj):

        user_dto = UserDto(
            name=user_obj.name,
            user_id=user_obj.id
        )
        print(user_dto)
        return user_dto


    def _get_project_details_dto(self,
                                 project_obj,
                                 user_dto,
                                 workflow_type_dto):

        project_details_dto = ProjectDto(
            name=project_obj.name,
            description=project_obj.description,
            workflow_type=workflow_type_dto,
            project_type=project_obj.project_type,
            user=user_dto,
            created_at=project_obj.created_at
        )

        return project_details_dto


    def is_valid_project_id(self, workflow_type: int):

        is_workflow_type_id_valid = Workflow.objects. \
            filter(id=workflow_type).exists()

        return is_workflow_type_id_valid
