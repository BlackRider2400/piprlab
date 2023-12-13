class Song:

    def __init__(self, title, year, time, is_vocal):
        """
        Args:
            time: is tuple(minute, seconds)
            is_vocal: True if song have vocals and False if not
        """
        if type(is_vocal) != bool:
            raise TypeError(f"is_vocal variable can not be {type(is_vocal)}")
        self._title = title
        self._year = year
        self._time = time
        self._is_vocal = is_vocal

    def get_title(self):
        return self._title

    def get_year(self):
        return self._year

    def get_time(self):
        return self._time

    def get_is_vocal(self):
        return self._is_vocal

