from song import Song


class Event:

    def __init__(self, songs):
        self._songs = sorted(songs, key=lambda song: song.get_year())

    def get_songs(self):
        return self._songs

    def add_song(self, song):
        if type(song) == Song:
            self._songs.append(song)
            self._songs = sorted(self._songs, key=lambda i: i.get_year())
            return 1
        return 0

    def remove_song(self, song):
        if type(song) == Song and song in self._songs:
            self._songs.remove(song)
            return 1
        return 0

    def calculate_time(self):
        time = [10, 0]
        for i in self._songs:
            time[0] += i.get_time()[0]
            time[1] += i.get_time()[1]
            if time[1] >= 60:
                time[1] = 0
                time[0] += 1

            if i.get_is_vocal:
                time[0] += 3
            else:
                time[0] += 2
        return time

    def get_special_song(self):
        """
        Returns:
        Song which has biggest differance in average time of song in whole event
        """
        whole_time = 0
        average = 0
        special_song = 0
        special_differance = 0
        for i in self.get_songs():
            whole_time += i.get_time()[0] * 60 + i.get_time()[1]

        average = whole_time / len(self._songs)

        for i in self.get_songs():
            time_in_s = i.get_time()[0] * 60 + i.get_time()[1]
            if abs(average - time_in_s) > special_differance:
                special_song = i
                special_differance = abs(average - time_in_s)

        return special_song

    def get_timetable_vocal(self):
        timetable = ""
        list = self._songs.copy()
        for i in list:
            timetable += "* " + str(i.get_title()) + "\n"

        return timetable

    def get_timetable_not_vocal(self):
        timetable = ""
        list = self._songs.copy()
        for i in list:
            if not i.get_is_vocal():
                timetable += "* " + str(i.get_title()) + "\n"

        return timetable
