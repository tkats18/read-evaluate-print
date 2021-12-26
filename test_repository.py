import os

from repl_dto import DatabaseInsertObject
from storage import IJsonStorageSystem


def test_repository_init():
    IJsonStorageSystem("./data/test.json", True)
    os.remove("./data/test.json")


def test_repository_add_simple():
    repo = IJsonStorageSystem("./data/test.json", True)
    repo.add_item(DatabaseInsertObject("obj1"))
    assert len(repo.get_all_content()) == 1
    os.remove("./data/test.json")


def test_repository_add_check():
    repo = IJsonStorageSystem("./data/test.json", True)
    repo.add_item(DatabaseInsertObject("obj1"))
    it = repo.get_top_item_with_data("obj1")

    assert len(repo.get_all_content()) == 1
    assert it.data == "obj1"

    os.remove("./data/test.json")


def test_repository_add_check_double():
    repo = IJsonStorageSystem("./data/test.json", True)
    repo.add_item(DatabaseInsertObject("obj1"))
    repo.add_item(DatabaseInsertObject("obj2"))

    it_1 = repo.get_top_item_with_data("obj1")
    it_2 = repo.get_top_item_with_data("obj2")

    assert len(repo.get_all_content()) == 2
    assert it_1.data == "obj1"
    assert it_2.data == "obj2"

    os.remove("./data/test.json")


def test_repository_add_check_quadriple():
    repo = IJsonStorageSystem("./data/test.json", True)

    repo.add_item(DatabaseInsertObject("obj1"))
    it_1 = repo.get_top_item_with_data("obj1")

    repo.add_item(DatabaseInsertObject("obj2"))
    it_2 = repo.get_top_item_with_data("obj2")

    assert len(repo.get_all_content()) == 2
    assert it_1.data == "obj1"
    assert it_2.data == "obj2"
    assert repo.get_item_with_id(it_1.id).id == it_1.id
    assert repo.get_item_with_id(it_2.id).id == it_2.id

    os.remove("./data/test.json")


def test_repository_add_check_cycle():
    repo = IJsonStorageSystem("./data/test.json", True)

    for i in range(10):
        repo.add_item(DatabaseInsertObject("obj" + str(i)))

    assert len(repo.get_all_content()) == 10

    for index, i in enumerate(repo.get_all_content()):
        assert i.data == "obj" + str(index)
        assert repo.get_item_with_id(i.id).id == i.id

    os.remove("./data/test.json")
