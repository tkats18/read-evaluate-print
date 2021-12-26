from dataclasses import dataclass

from REPlDto import DatabaseInsertObject, DatabaseResponseObject, CommandDTO
from Storage import IRepository

@dataclass
class CommandStorage:
    inner_storage: IRepository

    def get_command_by_name(self, name: str) -> CommandDTO:
        dto = self.inner_storage.get_item_with_data(name)
        return self._to_command(dto)

    def get_command_by_index(self, index: int) -> CommandDTO:
        dto = self.inner_storage.get_item_with_id(index)
        return self._to_command(dto)

    def get_content_num(self) -> int:
        return len(self.inner_storage.get_all_content())

    def add_command(self, command: str) -> None:
        self.inner_storage.add_item(DatabaseInsertObject(command))

    def _to_command(self, db_object: DatabaseResponseObject) -> CommandDTO:
        return CommandDTO(db_object.id, db_object.data)
