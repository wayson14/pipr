import pytest
from item import Item, Container


def test_item_default():
    item = Item()
    assert item.weight() == 0.1


def test_item_negative_or_zero_weight():
    with pytest.raises(ValueError):
        item = Item(weight=-5)

    with pytest.raises(ValueError):
        item = Item(weight=0)


def test_item_string_weight():
    with pytest.raises(TypeError):
        item = Item(weight="a")


def test_container_default():
    container = Container()
    assert container.weight() == 0.1
    assert container.max_load() == 0.5
    assert container.items() == []


# def test_container_weight_not_nested():
#     container = Container(weight=0.5)
#     assert container.weight() == 0.5


def test_container_nested_weight():
    item = Item(weight=0.5)
    inner_container = Container(weight=0.1, items=[item], max_load=1)
    outer_container = Container(weight=0.2, items=[inner_container], max_load=1)
    assert outer_container.weight() == 0.8


def test_container_wrong_item_types():
    item = Item()
    with pytest.raises(TypeError):
        container = Container(items=["a"])
    with pytest.raises(TypeError):
        container = Container(items=[5])
    with pytest.raises(TypeError):
        container = Container(items=[5, [], item])
    with pytest.raises(TypeError):
        container = Container(items=[[item]])


def test_container_max_load():
    container = Container(max_load=5)
    assert container.max_load() == 5


def test_container_wrong_max_load():
    with pytest.raises(TypeError):
        container = Container(max_load="a")
    with pytest.raises(ValueError):
        container = Container(max_load=-5)


def test_container_exceeded_max_load():
    item = Item(weight=0.7)
    with pytest.raises(ValueError):
        container = Container(max_load=0.5, items=[item])


def test_container_put_normal():
    item = Item()
    container = Container()
    container.put(item)
    assert container.weight() == 0.2


def test_container_wrong_put_input():
    container = Container()
    with pytest.raises(TypeError):
        container.put("a")
