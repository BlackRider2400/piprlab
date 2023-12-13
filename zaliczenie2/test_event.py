from song import Song
from event import Event


def test_get_songs():
    list_sorted = [Song("Abc", 1990, (2, 30), True), Song("Def", 1995, (2, 30), True), Song("Mno", 2020, (2, 30), True)]
    list = [Song("Mno", 2020, (2, 30), True), Song("Def", 1995, (2, 30), True), Song("Abc", 1990, (2, 30), True)]
    event = Event(list)
    for i in range(0, len(list_sorted) - 1):
        assert event.get_songs()[i].get_year() == list_sorted[i].get_year()


def test_add_song():
    song = Song("Xyz", 1991, (3, 49), False)
    list_sorted = [Song("Abc", 1990, (2, 30), True), song, Song("Def", 1995, (2, 30), True), Song("Mno", 2020, (2, 30), True)]
    list = [Song("Mno", 2020, (2, 30), True), Song("Def", 1995, (2, 30), True), Song("Abc", 1990, (2, 30), True)]
    event = Event(list)
    event.add_song(song)
    for i in range(0, len(list_sorted) - 1):
        assert event.get_songs()[i].get_year() == list_sorted[i].get_year()


def test_remove_song():
    song = Song("Xyz", 1991, (3, 49), False)
    list = [Song("Mno", 2020, (2, 30), True), song, Song("Def", 1995, (2, 30), True), Song("Abc", 1990, (2, 30), True)]
    list_copy = list.copy()
    event = Event(list)
    event.remove_song(song)
    assert len(list) - 1 == len(event.get_songs())
    assert song not in event.get_songs()


def test_calculate_time():
    list = [Song("Mno", 2020, (2, 30), True), Song("Def", 1995, (3, 39), True), Song("Abc", 1990, (2, 21), True)]
    event = Event(list)
    assert event.calculate_time()[0] == (10 + 2 + 2 + 3 + 3 + 3 + 3 + 1)
    assert event.calculate_time()[1] == 30


def test_get_special_song():
    list = [Song("Mno", 2020, (2, 30), True), Song("Def", 1995, (3, 39), True), Song("Abc", 1990, (2, 21), True)]
    event = Event(list)
    assert event.get_special_song().get_title() == "Def"


def test_get_timetable_vocal():
    list = [Song("Mno", 2020, (2, 30), True), Song("Def", 1995, (3, 39), False), Song("Abc", 1990, (2, 21), True)]
    event = Event(list)
    assert event.get_timetable_vocal() == "* Abc\n* Def\n* Mno\n"


def test_get_timetable_not_vocal():
    list = [Song("Mno", 2020, (2, 30), True), Song("Def", 1995, (3, 39), False), Song("Abc", 1990, (2, 21), True)]
    event = Event(list)
    assert event.get_timetable_not_vocal() == "* Def\n"
