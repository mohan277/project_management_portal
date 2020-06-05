from typing import List
from project_management_portal.models import User, Project, Workflow
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


    def is_valid_user_ids_list(self, assigned_to: List[int]):

        user_ids = User.objects.filter(id__in=assigned_to).values_list('id', flat=True)
        is_valid_list_of_user_ids = set(user_ids) == set(assigned_to)

        return is_valid_list_of_user_ids


    def is_admin(self, user_id: int):
        is_admin = User.objects.get(id=user_id).is_admin
        return is_admin


    def create_project(self,
                       name: str,
                       user_id: int,
                       description: str,
                       workflow_type: int,
                       project_type: str,
                       assigned_to: List[int]):


        project_obj = Project.objects.create(
            name=name,
            created_by_id=user_id,
            description=description,
            workflow_type_id=workflow_type,
            project_type=project_type)

        list_of_members_to_assign = User.objects.filter(id__in=assigned_to)

        project_obj.assigned_to.set(list_of_members_to_assign)

        project_details_dto = self._get_project_details_dto(project_obj)

        return project_details_dto


    def is_valid_limit(self, limit: int) -> bool:

        is_valid_limit = limit>=0
        return is_valid_limit


    def is_valid_offset(self, offset:int) -> bool:

        is_valid_offset = offset>=0
        return is_valid_offset


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
                    created_by=project_obj.created_by.username,
                    created_at=project_obj.created_at,
                    description=project_obj.description,
                    project_type=project_obj.project_type,
                    workflow_type=project_obj.workflow_type.name)

        return project_details_dto
