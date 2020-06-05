from typing import List
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
    INVALID_TASK_ID
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
    ListOfToStatesDto
)


class PresenterImplementation(PresenterInterface):

    def raise_invalid_username(self, username: str):
        raise NotFound(*INVALID_USERNAME)


    def raise_invalid_password(self, username: str, password: str):
        raise BadRequest(*INVALID_PASSWORD)


    def get_access_token(self, access_token: str):
        pass


    def raise_invalid_workflow_type_id_exception(self):
        raise NotFound(*INVALID_WORKFLOW_TYPE)



    def raise_invalid_list_of_user_ids_exception(self):
        raise NotFound(*INVALID_LIST_OF_USER_IDS)



    def get_create_project_response(self, project_details_dto: ProjectDto):

        response = {
            "name": project_details_dto.name,
            "project_id": project_details_dto.project_id,
            "description": project_details_dto.description,
            "workflow_type": project_details_dto.workflow_type,
            "project_type": project_details_dto.project_type,
            "created_by": project_details_dto.created_by.,
            "created_at": project_details_dto.created_at
        }
        return response


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


    def get_create_task_response(self, task_details_dto: TaskDto):

        project_dict = self._get_project_dict(
            task_details_dto.project)

        state_dict = self._get_state_dict(
            task_details_dto.state)

        response = {
            "title": task_details_dto.title,
            "description": task_details_dto.description,
            "project": project_dict,
            "state": state_dict,
            "issue_type": task_details_dto.issue_type
        }
        return response


    def get_list_of_tasks_response(
        self, list_of_tasks_dto: ListOfTasksDto):

        list_of_task_dicts = []
        list_of_tasks_dto = list_of_tasks_dto.tasks_dto
        for task_dto in list_of_tasks_dto:
            list_of_task_dicts.append(
                self.get_create_task_response(task_dto)
            )
        return list_of_task_dicts


    @staticmethod
    def _get_project_dict(project_dto: TaskProjectDto):

        project_dict = {
            "name": project_dto.name,
            "project_id": project_dto.project_id
        }

        return project_dict

    @staticmethod
    def _get_state_dict(state_dto: StateDto):

        state_dict = {
            "name": state_dto.name,
            "state_id": state_dto.state_id
        }

        return state_dict


    def get_create_transition_response(self,
                                       transition_details_dto: TransitionDto):

            from_state_dict = self._get_from_state_dict(
                transition_details_dto.from_state)

            to_state_dict = self._get_to_state_dict(
                transition_details_dto.to_state)

            response = {
                "name": transition_details_dto.name,
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
