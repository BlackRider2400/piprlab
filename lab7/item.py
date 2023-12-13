class Item:
    def __init__(self, name, mass):
        self._name = name
        if mass <= 0:
            raise ValueError
        self._mass = mass

    def get_name(self):
        return self._name

    def get_mass(self):
        return self._mass

    def set_name(self, name):
        self._name = name

    def set_mass(self, mass):
        if mass <= 0:
            raise ValueError
        self._mass = mass

    def __str__(self):
        return f"Name: {self._name} Mass: {self._mass} kg "
