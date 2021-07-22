from typing import List
from project_management_portal.models import Project, Workflow, Developer
from project_management_portal.interactors.storages. \
    project_storage_interface import ProjectStorageInterface
from project_management_portal.exceptions import \
    InvalidWorkflowIdException, InvalidListOfUserIdsException
from project_management_portal.interactors.storages.dtos import \
    ProjectDto, ListOfProjectsDto


class ProjectStorageImplementation(ProjectStorageInterface):

    def is_valid_workflow_type_id(self, workflow_type: int):

        is_workflow_type_id_valid = Workflow.objects. \
            filter(id=workflow_type).exists()

        return is_workflow_type_id_valid


    def create_project(self,
                       name: str,
                       user_id: int,
                       description: str,
                       project_type: str,
                       workflow_type: int,
                       developers: List[int]):


        project_obj = Project.objects.create(
            name=name,
            created_by_id=user_id,
            description=description,
            project_type=project_type,
            workflow_type_id=workflow_type)

        Developer.objects.create(project_id=project_obj.id, user_id=user_id)
        developer_instances = [Developer(project_id=project_obj.id, user_id=user_id)
            for user_id in developers]
        developer_objs = Developer.objects.bulk_create(developer_instances)

        project_details_dto = self._get_project_details_dto(project_obj)

        return project_details_dto

    def get_list_of_admin_projects(
        self, limit: int, offset: int, user_id: int) -> ListOfProjectsDto:

        list_of_project_objs = Project.objects.filter(
            created_by_id=user_id)


        list_of_project_dtos = self._get_list_of_project_dtos(
            list_of_project_objs[offset:offset+limit])

        total_count_of_projects= len(list_of_project_objs)

        list_of_projects_dto = ListOfProjectsDto(
            list_of_project_dtos=list_of_project_dtos,
            total_count_of_projects=total_count_of_projects
        )

        return list_of_projects_dto


    def get_list_of_member_projects(
        self, limit: int, offset: int, user_id: int) -> ListOfProjectsDto:

        list_of_project_objs = Project.objects.filter(
            assigned_to__id=user_id)

        total_count_of_projects= len(list_of_project_objs)

        list_of_project_dtos = self._get_list_of_project_dtos(
            list_of_project_objs[offset:offset+limit])

        list_of_projects_dto = ListOfProjectsDto(
            list_of_project_dtos=list_of_project_dtos,
            total_count_of_projects=total_count_of_projects
        )

        return list_of_projects_dto


    def _get_list_of_project_dtos(self, project_objs):

            list_of_project_dtos = []

            for project_obj in project_objs:

                project_dto = self._get_project_details_dto(project_obj)

                list_of_project_dtos.append(project_dto)

            return list_of_project_dtos


    def _get_project_details_dto(self, project_obj):

        project_details_dto = ProjectDto(
                    name=project_obj.name,
                    project_id=project_obj.id,
                    created_by_id=project_obj.created_by_id,
                    created_at=project_obj.created_at,
                    description=project_obj.description,
                    project_type=project_obj.project_type,
                    workflow_type=project_obj.workflow_type.name)

        return project_details_dto


    def get_user_ids(self, project_id: int) -> List[int]:

        user_ids = Developer.objects.filter(
            project_id=project_id).values('user_id', flat=True)
        return user_ids
