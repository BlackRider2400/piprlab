from item import Item


class Container(Item):
    def __init__(self, name, mass, load_capacity):
        super().__init__(name, mass)
        if load_capacity < mass:
            raise ValueError
        self._load_capacity = load_capacity
        self._weight = mass
        self._items = []

    def get_load_capacity(self):
        if self._load_capacity < self._mass:
            raise ValueError
        return self._load_capacity

    def set_load_capacity(self, load_capacity):
        self._load_capacity = load_capacity

    def get_weight(self):
        return self._weight

    def set_weight(self, weight):
        if weight < self._mass:
            raise ValueError
        self._weight = weight

    def get_items(self):
        return self._items

    def add_item(self, item):
        if self._weight + item.get_mass() <= self._load_capacity:
            self._weight += item.get_mass()
            self._items.append(item)
            return True
        return False

    def delete_item(self, item):
        if item in self._items:
            self._items.remove(item)
            self._weight -= item.get_mass()
            return True
        return False

    def __str__(self):
        return "Container = " + super().__str__() + f"Load capacity: {self._load_capacity} Weight: {self._weight} " \
                                                    f"Items: {self._items}"

