from django.contrib import admin
from project_management_portal.models import (
    Task,
    State,
    Project,
    Workflow,
    Checklist,
    Transition,
)


admin.site.register(Task)
admin.site.register(State)
admin.site.register(Project)
admin.site.register(Workflow)
admin.site.register(Checklist)
admin.site.register(Transition)