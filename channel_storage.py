from dataclasses import dataclass
from typing import Optional, Protocol

from repl_dto import ChannelDTO, DatabaseInsertObject, DatabaseResponseObject
from storage import IRepository


class IChannelStorage(Protocol):
    def get_channel_by_name(self, name: str) -> Optional[ChannelDTO]:
        pass

    def add_channel(self, name: str) -> None:
        pass


@dataclass
class ChannelStorage:
    inner_storage: IRepository

    def get_channel_by_name(self, name: str) -> Optional[ChannelDTO]:
        dto = self.inner_storage.get_top_item_with_data(name)

        if dto is None:
            return None

        return self._to_channel(dto)

    def add_channel(self, name: str) -> None:
        self.inner_storage.add_item(DatabaseInsertObject(name))

    def _to_channel(self, db_object: DatabaseResponseObject) -> ChannelDTO:
        return ChannelDTO(db_object.id, db_object.data)
