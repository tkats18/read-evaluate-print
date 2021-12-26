from dataclasses import dataclass

from REPlDto import DatabaseResponseObject, UserDTO, DatabaseInsertObject
from Storage import IRepository


@dataclass
class UserStorage:
    inner_storage: IRepository

    def get_user_by_name(self, name: str) -> UserDTO:
        dto = self.inner_storage.get_item_with_data(name)
        return self._to_user(dto)

    def add_user(self, name: str) -> None:
        self.inner_storage.add_item(DatabaseInsertObject(name))

    def _to_user(self, db_object: DatabaseResponseObject) -> UserDTO:
        return UserDTO(db_object.id, db_object.data)

# აპლიკაციის დაწერა

# ობზერვერის დაწერა
# ტესტები
# formatter
