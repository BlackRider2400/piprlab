import pytest

from song import Song


def test_create_song():
    song = Song("Jungle Girl", 2022, (2, 48), True)
    assert song.get_title() == "Jungle Girl"
    assert song.get_year() == 2022
    assert song.get_time() == (2, 48)
    assert song.get_is_vocal()


def test_create_with_issue_song():
    with pytest.raises(TypeError):
        song = Song("Jungle Girl", 2022, (2, 48), 420)
        assert song.get_title() == "Jungle Girl"
        assert song.get_year() == 2022
        assert song.get_time() == (2, 48)
        assert song.get_is_vocal()
