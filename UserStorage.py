from REPlDto import DatabaseResponseObject, UserDTO, DatabaseInsertObject
from Storage import IRepository


class UserStorageAdapter:
    inner_storage: IRepository

    def get_user_by_name(self, name: str) -> UserDTO:
        dto = self.inner_storage.get_item_with_data(name)
        return self._to_user(dto)

    def add_user(self, name: str) -> None:
        self.inner_storage.add_item(DatabaseInsertObject(name))

    def _to_user(self, db_object: DatabaseResponseObject) -> UserDTO:
        return UserDTO(db_object.id, db_object.data)

# სამივე სთორჯის დამთავრება
# დამატება სთორეჯებში
# სთორეჯიდან ბრუნდებოდეს კლასი რომელსაც ექნება toUser toChannel... და ექნება დეფაულტები რაც მაქ : id , key
# გაპარსვის დაწერა
# ინფუთ სტრატეგიის გადახედვა
# აპლიკაციის დაწერა

# კომანდების დაწერა
# ობზერვერის დაწერა
# ტესტები
# formatter