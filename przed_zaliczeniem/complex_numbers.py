
class ComplexNumber:

    def __init(self, rz, im):
        if (type(rz) == float or type(rz) == int) and (type(im) == float or type(im) == int):
            self._rz = rz
            self._im = im
        else:
            raise ValueError

    def get_rz(self):
        return self._rz

    def get_im(self):
        return self._im

    def set_rz(self, rz):
        if type(rz) == int or type(rz) == float:
            self._rz = rz
        else:
            raise ValueError

    def set_im(self, im):
        if type(im) == int or type(im) == float:
            self._im = im
        else:
            raise ValueError

    def __str__(self):
        if self._im > 0:
            return f"{self._rz} + {self._im} * √-1"
        elif self._im < 0:
            return f"{self._rz} - {self._im} * √-1"
        else:
            return f"{self._rz}"


    def add_by(self, complex):
        if type(complex) != ComplexNumber:
            raise ValueError

        self._rz += complex.get_rz()
        self._im += complex.get_im()


