import enum
from ib_common.constants import BaseEnumClass


class ProjectType(BaseEnumClass, enum.Enum):
    CLASSICSOFTWARE = "Classic Software"
    FINANCIAL = "Financial"
    CRM = "CRM"


class IssueType(BaseEnumClass, enum.Enum):
    TASK = "Task"
    BUG = "Bug"
    DEVELOPER_STORY = "Developer story"
    USER_STORY = "User story"
    ENHANCEMENT = "Enhancement"
