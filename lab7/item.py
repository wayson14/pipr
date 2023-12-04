# Zaprojektuj i wykonaj klasy reprezentujące przedmiot o masie podanej w
# kilogramach oraz pojemnik (który sam jest przedmiotem) o podanym udźwigu.
# Przedmioty można wkładać i wyjmować z pojemników, o ile są one w ramach
# dopuszczalnego udźwigu (w przeciwnym razie nie udaje się włożyć przedmiotu do
# pojemnika). Program ma umożliwić wypisanie zawartości każdego pojemnika w
# postaci zestawu mas przedmiotów, które się w nim znajdują.

# pamiętaj o tym, że box może mieć swoją wagę, którą należy uwzględnić
# box może mieć również różne pojemniki w sobie samym


class Item:
    def __init__(self, weight=0.1, name="DefaultItem"):
        if not name:
            raise ValueError("Name cannot be empty")
        if weight < 0:
            raise ValueError("Weight cannot be 0 or negative")
        self._weight = weight
        self._name = name

    def weight(self):
        return self._weight

    def name(self):
        return self._name


class Container(Item):
    def __init__(self, items, max_load):
        if not items:
            items = []
        super().__init__()
        self._items = items
        self._max_load = max_load
        if sum(items._weight) > max_load:
            raise ValueError(
                "Sum of items' weights cannot be"
                + "greater than max load of a container"
            )

    def _check_if_item_fits(self, item):
        if self.max_load + item.weight() > self._max_load:
            return False
        else:
            return True

    def put_item_into_container(self, item):
        if not self._check_if_item_fits(item):
            raise ValueError("Weight of a specified item is too big")
        self._items.append(item)

    def show_items(self):
        for name, weight in zip(self._items.name(), self._items.weight()):
            print(f"{name}: {weight}")
