from typing import List
from project_management_portal.constants.constants import DEFAULT_DATE_TIME_FORMAT
from project_management_portal.interactors.presenters.presenter_interface \
    import PresenterInterface
from django_swagger_utils.drf_server.exceptions import NotFound, BadRequest
from project_management_portal.constants.exception_messages import (
    INVALID_USERNAME,
    INVALID_PASSWORD,
    INVALID_WORKFLOW_TYPE,
    INVALID_PROJECT,
    INVALID_FROM_STATE,
    INVALID_TO_STATE,
    INVALID_STATE,
    INVALID_LIST_OF_USER_IDS,
    INVALID_TASK_ID,
    INVALID_ADMIN,
    INVALID_USER,
    INVALID_LIMIT_VALUE,
    INVALID_OFFSET_VALUE
)
from project_management_portal.interactors.storages.dtos import (
    UserDto,
    TaskDto,
    StateDto,
    ProjectDto,
    ToStateDto,
    FromStateDto,
    TransitionDto,
    ListOfTasksDto,
    TaskProjectDto,
    WorkflowTypeDto,
    ListOfProjectsDto,
    ListOfWorkflowsDto,
    ListOfToStatesDto,
    ListOfChecklistsDto,
    FinalProjectDTO,
    FinalUserDTO
)


class PresenterImplementation(PresenterInterface):

    def raise_invalid_username(self):
        raise NotFound(*INVALID_USERNAME)


    def raise_invalid_password(self):
        raise BadRequest(*INVALID_PASSWORD)

    def get_access_token(self, access_token:str, is_admin: bool):
        authorization_details = {
            "access_token": access_token,
            "is_admin": is_admin
        }
        return authorization_details


    def raise_invalid_workflow_type_id_exception(self):
        raise NotFound(*INVALID_WORKFLOW_TYPE)

    def raise_invalid_admin_exception(self):
        raise NotFound(*INVALID_ADMIN)


    def get_create_project_response(
        self, final_project_details_dto: FinalProjectDTO):
        project_details_dto = final_project_details_dto.project_details_dto
        user_details_dtos = final_project_details_dto.user_details_dtos

        response = {
            "name": project_details_dto.name,
            "project_id": project_details_dto.project_id,
            "description": project_details_dto.description,
            "workflow_type": project_details_dto.workflow_type,
            "project_type": project_details_dto.project_type,
            "created_by_id": project_details_dto.created_by_id,
            "created_at": project_details_dto.created_at.strftime(
                DEFAULT_DATE_TIME_FORMAT
            ),
            "developers": self.get_user_details(
                user_dtos=user_details_dtos
            )
        }
        return response

    def get_user_details(self, user_dtos: List[FinalUserDTO]):
        list_of_user_details = [
            {
                "name": user_dto.name,
                "user_id": user_dto.user_id,
                "is_admin": user_dto.is_admin,
                "profile_pic_url": user_dto.profile_pic_url
            }
            for user_dto in user_dtos
        ]
        return list_of_user_details

    def raise_invalid_limit_value_exception(self):
        raise BadRequest(*INVALID_LIMIT_VALUE)


    def raise_invalid_offset_value_exception(self):
        raise BadRequest(*INVALID_OFFSET_VALUE)



    def get_list_of_projects_response(
        self, list_of_projects_dto: ListOfProjectsDto):

        list_of_projects_dict = []
        list_of_project_dtos = list_of_projects_dto.list_of_project_dtos
        for project_dto in list_of_project_dtos:
            list_of_projects_dict.append(
                self.get_create_project_response(project_dto)
            )

        response = {
            "projects": list_of_projects_dict,
            "total_count_of_projects": list_of_projects_dto. \
                total_count_of_projects
        }

        return response


    def raise_invalid_project_id_exception(self):
        raise NotFound(*INVALID_PROJECT)


    def raise_invalid_state_id_exception(self):
        raise NotFound(*INVALID_STATE)


    def raise_invalid_user_id_exception(self):
        raise NotFound(*INVALID_USER)


    def get_create_task_response(self, task_details_dto: TaskDto):

        response = {
            "task_id": task_details_dto.task_id,
            "title": task_details_dto.title,
            "description": task_details_dto.description,
            "project": task_details_dto.project,
            "state": task_details_dto.state,
            "created_by_id": task_details_dto.created_by_id,
            "issue_type": task_details_dto.issue_type,
            "created_at": task_details_dto.created_at.strftime(
                DEFAULT_DATE_TIME_FORMAT)
        }
        return response


    def get_list_of_tasks_response(
        self, list_of_tasks_dto: ListOfTasksDto):

        list_of_tasks_dict = []
        list_of_task_dtos = list_of_tasks_dto.list_of_task_dtos
        for task_dto in list_of_task_dtos:
            list_of_tasks_dict.append(
                self.get_create_task_response(task_dto)
            )

        response = {
            "tasks": list_of_tasks_dict,
            "total_count_of_tasks": list_of_tasks_dto.total_count_of_tasks
        }

        return response


    def get_create_transition_response(self,
                                       transition_details_dto: TransitionDto):

            from_state_dict = self._get_from_state_dict(
                transition_details_dto.from_state)

            to_state_dict = self._get_to_state_dict(
                transition_details_dto.to_state)

            response = {
                "name": transition_details_dto.name,
                "transition_id": transition_details_dto.transition_id,
                "description": transition_details_dto.description,
                "from_state": from_state_dict,
                "to_state": to_state_dict
            }
            return response


    @staticmethod
    def _get_from_state_dict(from_state_dto: FromStateDto):

        from_state_dict = {
            "name": from_state_dto.name,
            "from_state_id": from_state_dto.from_state_id
        }

        return from_state_dict


    @staticmethod
    def _get_to_state_dict(to_state_dto: ToStateDto):

        to_state_dict = {
            "name": to_state_dto.name,
            "to_state_id": to_state_dto.to_state_id
        }

        return to_state_dict


    def raise_invalid_from_state_id_exception(self):
        raise NotFound(*INVALID_FROM_STATE)


    def raise_invalid_to_state_id_exception(self):
        raise NotFound(*INVALID_TO_STATE)


    def get_list_of_workflows_response(
        self, list_of_workflows_dto: ListOfWorkflowsDto):

        list_of_workflows_dict = []
        list_of_workflow_dtos = list_of_workflows_dto.list_of_workflow_dtos
        for workflow_dto in list_of_workflow_dtos:
            list_of_workflows_dict.append(
                self._get_workflow_response(workflow_dto)
            )

        response = {
            "workflows": list_of_workflows_dict,
            "total_count_of_workflows": list_of_workflows_dto. \
                total_count_of_workflows
        }

        return response


    @staticmethod
    def _get_workflow_response(workflow_dto):

        response = {
            "name": workflow_dto.name,
            "workflow_id": workflow_dto.workflow_id
        }
        return response


    def raise_invalid_task_id_exception(self):
        raise NotFound(*INVALID_TASK_ID)


    def get_to_states_based_on_current_state_response(
        self, list_of_to_states_dto: ListOfToStatesDto):

        list_of_to_states_dict = []
        list_of_to_state_dtos = list_of_to_states_dto.list_of_to_state_dtos
        for to_state_dto in list_of_to_state_dtos:
            list_of_to_states_dict.append(
                self._get_to_states_response(to_state_dto)
            )

        total_count_of_to_states = len(list_of_to_states_dict)

        response = {
            "to_states": list_of_to_states_dict,
            "total_count_of_to_states": total_count_of_to_states
        }

        return response


    @staticmethod
    def _get_to_states_response(to_state_dto):

        response = {
            "name": to_state_dto.name,
            "to_state_id": to_state_dto.to_state_id
        }
        return response


    def get_transition_details_between_two_states_response(
        self, list_of_checklists_dto: ListOfChecklistsDto):

        list_of_checklists_dict = []
        list_of_checklist_dtos = list_of_checklists_dto.list_of_checklist_dtos

        for checklist_dto in list_of_checklist_dtos:
            list_of_checklists_dict.append(
                self._get_checklist_response(checklist_dto)
            )

        response = {
            "checklists": list_of_checklists_dict
        }
        return response

    @staticmethod
    def _get_checklist_response(checklist_dto):

        response = {
            "name": checklist_dto.name,
            "checklist_id": checklist_dto.checklist_id,
            "is_mandatory": checklist_dto.is_mandatory
        }
        return response
