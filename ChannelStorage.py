from dataclasses import dataclass

from REPlDto import ChannelDTO, DatabaseInsertObject, DatabaseResponseObject
from Storage import IRepository


@dataclass
class ChannelStorage:
    inner_storage: IRepository

    def get_channel_by_name(self, name: str) -> ChannelDTO:
        dto = self.inner_storage.get_item_with_data(name)
        return self._to_channel(dto)

    def add_channel(self, name: str) -> None:
        self.inner_storage.add_item(DatabaseInsertObject(name))

    def _to_channel(self, db_object: DatabaseResponseObject) -> ChannelDTO:
        return ChannelDTO(db_object.id, db_object.data)
