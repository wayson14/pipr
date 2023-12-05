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
        if max_load < 0:
            raise ValueError(f"Max load cannot be negative - provided {max_load}")

        for item in items:
            self._check_if_valid_item(item)
        self._check_if_not_exceed_max_load_initial(items, weight, max_load)
        self._max_load = max_load
        self._items = items

    def _check_if_valid_item(self, item):
        if not isinstance(item, Item):
            raise TypeError(f"{type(item)} is not a (sub)instance of {Item.__name__}")

    def _check_if_not_exceed_max_load(self, item):
        if self.weight() + item.weight() > self._max_load:
            raise ValueError(
                f"Adding this item would exceed " + "max load of the container"
            )

    def _check_if_not_exceed_max_load_initial(self, items, weight, max_load):
        items_sum_weight = sum(map(self._get_weight, items))
        if items_sum_weight + weight > max_load:
            raise ValueError(
                "Creating object with this item inside would exceed max load"
            )

    def _get_weight(self, item):
        return item.weight()

    def items(self):
        return self._items

    def weight(self):
        return sum(map(self._get_weight, self._items)) + self._weight

    def max_load(self):
        return self._max_load

    def put(self, item):
        self._check_if_valid_item(item)
        self._check_if_not_exceed_max_load(item)
        self._items.append(item)

    def pop(self, item):
        if not item in self.items():
            raise ValueError("Provided item not in a container")
        return self._items.pop(self._items.index(item))

    def _prepare_recursive_weight_tree(self, item, n=0, result_list=None):
        if result_list is None:
            result_list = []

        if not isinstance(item, Container) or len(item.items()) == 0:
            return [(item.weight(), n)]
        else:
            for inner_item in item.items():
                result_list.extend(
                    self._prepare_recursive_weight_tree(
                        inner_item, n + 1, result_list=[]
                    )
                )
            result_list.append((item._weight, n))
            return result_list

    def print_weights(self):
        tree = self._prepare_recursive_weight_tree(self)
        for 

item = Item()
item2 = Item()
container_inner = Container(items=[item, item2])
container_outer = Container(items=[container_inner])
r = container_outer.print_weights()
for result in r:
    print(result)
