import json
from dataclasses import dataclass
from typing import Protocol, List, Any

# id,content
from REPlDto import DatabaseResponseObject, DatabaseInsertObject


class IRepository(Protocol):

    def get_item_with_id(self, index: int) -> DatabaseResponseObject:
        pass

    def get_item_with_data(self, data: str) -> DatabaseResponseObject:
        pass

    def get_all_content(self) -> List[DatabaseResponseObject]:
        pass

    def add_item(self, data: DatabaseInsertObject) -> None:
        pass


@dataclass
class IJsonStorageSystem(IRepository):
    file_path: str
    # init TODO
    def get_item_with_id(self, index: int) -> DatabaseResponseObject:
        data_array = self.get_all_content()

        for i in data_array:
            if i.id == index:
                return i

        raise IndexError()

    def get_item_with_data(self, data: str) -> DatabaseResponseObject:
        data_array = self.get_all_content()

        for i in data_array:
            if i.data == data:
                return i

        raise IndexError()

    def get_all_content(self) -> List[DatabaseResponseObject]:
        return list(map(lambda data_item: self._to_database_object(data_item), self._get_data_content()))

    def add_item(self, data: DatabaseInsertObject) -> None:
        # TODO
        pass

    def _to_database_object(self, data_item) -> DatabaseResponseObject:
        res = DatabaseResponseObject(int(data_item["id"]), data_item["data"])
        return res

    def _get_data_content(self) -> Any:
        f = open(self.file_path)
        all_file_data = json.load(f)

        return all_file_data["data"]
