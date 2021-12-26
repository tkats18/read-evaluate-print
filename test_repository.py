import os

from repl_dto import DatabaseInsertObject
from storage import IJsonStorageSystem


def test_repository_init() -> None:
    IJsonStorageSystem("./data/test.json", True)
    os.remove("./data/test.json")


def test_repository_add_simple() -> None:
    repo = IJsonStorageSystem("./data/test.json", True)
    repo.add_item(DatabaseInsertObject("obj1"))
    assert len(repo.get_all_content()) == 1
    os.remove("./data/test.json")


def test_repository_add_check() -> None:
    repo = IJsonStorageSystem("./data/test.json", True)
    repo.add_item(DatabaseInsertObject("obj1"))
    it = repo.get_top_item_with_data("obj1")

    assert len(repo.get_all_content()) == 1
    assert it is not None and it.data == "obj1"

    os.remove("./data/test.json")


def test_repository_add_check_double() -> None:
    repo = IJsonStorageSystem("./data/test.json", True)
    repo.add_item(DatabaseInsertObject("obj1"))
    repo.add_item(DatabaseInsertObject("obj2"))

    it_1 = repo.get_top_item_with_data("obj1")
    it_2 = repo.get_top_item_with_data("obj2")

    assert len(repo.get_all_content()) == 2
    assert it_1 is not None and it_1.data == "obj1"
    assert it_2 is not None and it_2.data == "obj2"

    os.remove("./data/test.json")


def test_repository_add_check_quadriple() -> None:
    repo = IJsonStorageSystem("./data/test.json", True)

    repo.add_item(DatabaseInsertObject("obj1"))
    it_1 = repo.get_top_item_with_data("obj1")

    repo.add_item(DatabaseInsertObject("obj2"))
    it_2 = repo.get_top_item_with_data("obj2")

    assert len(repo.get_all_content()) == 2
    assert it_1 is not None and it_1.data == "obj1"
    assert it_2 is not None and it_2.data == "obj2"
    get_1 = repo.get_item_with_id(it_1.id)
    get_2 = repo.get_item_with_id(it_2.id)
    assert get_1 is not None and get_1.id == it_1.id
    assert get_2 is not None and get_2.id == it_2.id

    os.remove("./data/test.json")


def test_repository_add_check_cycle() -> None:
    repo = IJsonStorageSystem("./data/test.json", True)

    for i in range(10):
        repo.add_item(DatabaseInsertObject("obj" + str(i)))

    assert len(repo.get_all_content()) == 10

    index = 0
    for cur_db_object in repo.get_all_content():
        assert cur_db_object is not None and cur_db_object.data == "obj" + str(index)
        get_cur_db_with_id = repo.get_item_with_id(cur_db_object.id)
        assert (
            get_cur_db_with_id is not None and get_cur_db_with_id.id == cur_db_object.id
        )
        index += 1

    os.remove("./data/test.json")
