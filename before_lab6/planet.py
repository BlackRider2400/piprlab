class planeta:

    def __init__(self, nazwa, mefedron):
        self._nazwa = nazwa
        self._mefedron = mefedron

    def __str__(self):
        return f"To jest zajebista planeta: {self._nazwa} i ma {self._mefedron} mefedronu."

    def set_nazwa(self, nowa_nazwa):
        self._nazwa = nowa_nazwa

    def nazwa(self):
        return self._nazwa
