from dbService.models.userModel import UserModel

from typing import Optional


def add_new_user(t_id: int, name: str):
    user = UserModel.create(t_id=t_id, name=name)

    return user.get_id()


def get_user(t_id: int) -> Optional[UserModel]:
    return UserModel.get_or_none(t_id=t_id)
