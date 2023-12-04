import pytest
from item import Item, Container

def test_item_creation():
    item = Item(weight = 5, name = "Ball")
    assert item.weight() == 5
    assert item.name() == "Ball"

def test_negative_weight():
    with pytest.raises(ValueError):
        item = Item(weight = -5)

def test_empty_name():
    with pytest.raises(ValueError):
        item = Item(name = "")

def test_container_creation():
    container = Container(weight = 1, name = "Basic Container", )