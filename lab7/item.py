# Zaprojektuj i wykonaj klasy reprezentujące przedmiot o masie podanej w
# kilogramach oraz pojemnik (który sam jest przedmiotem) o podanym udźwigu.
# Przedmioty można wkładać i wyjmować z pojemników, o ile są one w ramach
# dopuszczalnego udźwigu (w przeciwnym razie nie udaje się włożyć przedmiotu do
# pojemnika). Program ma umożliwić wypisanie zawartości każdego pojemnika w
# postaci zestawu mas przedmiotów, które się w nim znajdują.

# pamiętaj o tym, że box może mieć swoją wagę, którą należy uwzględnić
# box może mieć również różne pojemniki w sobie samym


class Item:
    def __init__(self, weight=0.1):
        if weight <= 0:
            raise (ValueError("Weight cannot be 0 or negative!"))
        self._weight = weight

    def weight(self):
        return self._weight


class Container(Item):
    def __init__(self, weight=0.1, max_load=0.5, items=[]):
        super().__init__(weight)
        self._max_load = 0
        self._items = []

        if max_load < 0:
            raise ValueError(f"Max load cannot be negative - provided {max_load}")

        for item in items:
            self._check_if_valid_item(item)
            self._check_if_not_exceed_max_load(item)
        self._max_load = max_load
        self._items = items

    def _check_if_valid_item(self, item):
        if not isinstance(item, Item):
            raise TypeError(f"{type(item)} is not a (sub)instance of {Item.__name__}")

    def _check_if_not_exceed_max_load(
        self, item, weight=self._weight, max_load=self._max_load
    ):
        if weight + item.weight() > max_load:
            raise ValueError(
                f"Adding this item would exceed " + "max load of the container"
            )

    def items(self):
        return self._items

    def weight(self):
        def get_weight(item):
            return item.weight()

        return sum(map(get_weight, self.items())) + self._weight

    def max_load(self):
        return self._max_load

    def put(self, item):
        self._check_if_valid_item(item)
        self._items.append(item)

    # def print_weights(self):
    #     for item in self.items():
    #         print f"{item.__name__}: {item.weight()}"
