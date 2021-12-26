from dataclasses import dataclass
from typing import Optional, Protocol

from repl_dto import CommandDTO, DatabaseInsertObject, DatabaseResponseObject
from storage import IRepository


class ICommandStorage(Protocol):
    def get_command_by_name(self, name: str) -> Optional[CommandDTO]:
        pass

    def get_command_by_index(self, index: int) -> Optional[CommandDTO]:
        pass

    def get_content_num(self) -> int:
        pass

    def add_command(self, command: str) -> None:
        pass


@dataclass
class CommandStorage:
    inner_storage: IRepository

    def get_command_by_name(self, name: str) -> Optional[CommandDTO]:
        dto = self.inner_storage.get_top_item_with_data(name)

        if dto is None:
            return None

        return self._to_command(dto)

    def get_command_by_index(self, index: int) -> Optional[CommandDTO]:
        dto = self.inner_storage.get_item_with_id(index)

        if dto is None:
            return None

        return self._to_command(dto)

    def get_content_num(self) -> int:
        return len(self.inner_storage.get_all_content())

    def add_command(self, command: str) -> None:
        self.inner_storage.add_item(DatabaseInsertObject(command))

    def _to_command(self, db_object: DatabaseResponseObject) -> CommandDTO:
        return CommandDTO(db_object.id, db_object.data)
