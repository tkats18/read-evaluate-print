import json
import os
from typing import Protocol, List, Any, Optional

# id,content
from repl_dto import DatabaseResponseObject, DatabaseInsertObject


class IRepository(Protocol):

    def get_item_with_id(self, index: int) -> Optional[DatabaseResponseObject]:
        pass

    def get_item_with_data(self, data: str) -> Optional[DatabaseResponseObject]:
        pass

    def get_all_content(self) -> List[DatabaseResponseObject]:
        pass

    def add_item(self, data: DatabaseInsertObject) -> None:
        pass


class IJsonStorageSystem(IRepository):

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.max_id = 0
        mode = 'a' if os.path.exists(file_path) else 'w'

        if mode == 'w':
            with open(file_path, mode) as f:
                f.write("{\n\"data\":[\n]\n}")
        else:
            for i in self.get_all_content():
                self.max_id = max(i.id + 1, self.max_id)

    def get_item_with_id(self, index: int) -> Optional[DatabaseResponseObject]:
        data_array = self.get_all_content()

        for i in data_array:
            if i.id == index:
                return i

        return None

    def get_item_with_data(self, data: str) -> Optional[DatabaseResponseObject]:
        data_array = self.get_all_content()

        for i in data_array:
            if i.data == data:
                return i

        return None

    def get_all_content(self) -> List[DatabaseResponseObject]:
        return list(map(lambda data_item: self._to_database_object(data_item), self._get_data_content()))

    def add_item(self, insert_object: DatabaseInsertObject) -> None:
        f = open(self.file_path,"r+")
        all_file_data = json.load(f)
        new_object = {"id": self.max_id, "data": insert_object.data}
        all_file_data["data"].append(new_object)

        f.truncate()
        f.close()

        f = open(self.file_path,"r+")
        f.write(json.dumps(all_file_data,indent=4))
        self.max_id += 1

    def _to_database_object(self, data_item) -> DatabaseResponseObject:
        res = DatabaseResponseObject(int(data_item["id"]), data_item["data"])
        return res

    def _get_data_content(self) -> Any:
        f = open(self.file_path)
        all_file_data = json.load(f)

        return all_file_data["data"]
