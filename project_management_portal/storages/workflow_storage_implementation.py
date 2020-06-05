from typing import List
from project_management_portal.models import User, Project, Workflow
from project_management_portal.interactors.storages. \
    workflow_storage_interface import WorkflowStorageInterface
from project_management_portal.interactors.storages.dtos import \
    WorkflowDto, ListOfWorkflowsDto


class WorkflowStorageImplementation(WorkflowStorageInterface):

    def get_list_of_workflows(self) -> ListOfWorkflowsDto:

        list_of_workflow_objs = Workflow.objects.all()

        total_count_of_workflows = len(list_of_workflow_objs)

        list_of_workflow_dtos = self._get_list_of_workflow_dtos(
            list_of_workflow_objs)


        list_of_workflows_dto = ListOfWorkflowsDto(
            list_of_workflow_dtos=list_of_workflow_dtos,
            total_count_of_workflows=total_count_of_workflows
        )

        return list_of_workflows_dto


    def _get_list_of_workflow_dtos(self, workflow_objs):

            list_of_workflow_dtos = []

            for workflow_obj in workflow_objs:

                workflow_dto = self._get_workflow_details_dto(workflow_obj)

                list_of_workflow_dtos.append(workflow_dto)

            return list_of_workflow_dtos


    def _get_workflow_details_dto(self, workflow_obj):

        workflow_details_dto = WorkflowDto(name=workflow_obj.name,
                                           workflow_id=workflow_obj.id)

        return workflow_details_dto
