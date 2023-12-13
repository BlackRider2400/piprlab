import pytest

from item import Item
from containter import Container


def test_create_item():
    simple_item = Item("Apple", 1)
    assert simple_item.get_name() == "Apple"
    assert simple_item.get_mass() == 1


def test_create_no_mass_item():
    with pytest.raises(ValueError):
        weird_item = Item("Susy Apple", -10)


def test_create_container():
    simple_container = Container("Box", 10, 50)
    assert simple_container.get_load_capacity() == 50


def test_create_no_load_container():
    with pytest.raises(ValueError):
        weird_container = Container("Box", 10, -10)


def test_add_item_to_container():
    simple_item = Item("Apple", 1)
    simple_container = Container("Box", 10, 50)
    assert simple_container.add_item(simple_item) == True


def test_add_too_heavy_item():
    simple_item = Item("Apple", 100)
    simple_container = Container("Box", 10, 50)
    assert simple_container.add_item(simple_item) == False


def test_delete_item():
    simple_item = Item("Apple", 1)
    simple_container = Container("Box", 10, 50).add_item(simple_item)
    assert simple_container.del_item(simple_item) == True


def test_delete_item():
    simple_item = Item("Apple", 1)
    simple_item_v2 = Item("Banana", 2)
    simple_container = Container("Box", 10, 50)
    simple_container.add_item(simple_item)
    assert simple_container.delete_item(simple_item_v2) == False

