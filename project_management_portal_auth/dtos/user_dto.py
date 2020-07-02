from dataclasses import dataclass


@dataclass
class UserDTO:
    user_id: int
    name: str
    profile_pic_url: str
    is_admin: bool


@dataclass
class IsAdminDTO:
    is_admin: bool
