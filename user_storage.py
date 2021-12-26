from dataclasses import dataclass
from typing import Optional, Protocol

from repl_dto import DatabaseInsertObject, DatabaseResponseObject, UserDTO
from storage import IRepository


class IUserStorage(Protocol):
    def get_user_by_name(self, name: str) -> Optional[UserDTO]:
        pass

    def get_user_by_id(self, user_id: int) -> Optional[UserDTO]:
        pass

    def add_user(self, name: str) -> None:
        pass


@dataclass
class UserStorage:
    inner_storage: IRepository

    def get_user_by_name(self, name: str) -> Optional[UserDTO]:
        dto = self.inner_storage.get_top_item_with_data(name)
        if dto is None:
            return None
        return self._to_user(dto)

    def get_user_by_id(self, user_id: int) -> Optional[UserDTO]:
        dto = self.inner_storage.get_item_with_id(user_id)
        if dto is None:
            return None
        return self._to_user(dto)

    def add_user(self, name: str) -> None:
        self.inner_storage.add_item(DatabaseInsertObject(name))

    def _to_user(self, db_object: DatabaseResponseObject) -> UserDTO:
        return UserDTO(db_object.id, db_object.data)


# ტესტები
