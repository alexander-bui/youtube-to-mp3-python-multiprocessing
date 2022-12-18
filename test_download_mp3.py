"""
If you wish to run unit test, need pytest
pip install pytest
pytest
"""
import os
import pytest
from main import download_mp3


class Settings:
    youtube_urls = [
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    ]

    destination = "C:/test/downloads"

    prefix = "song_"


@pytest.fixture
def settings():
    return Settings()


def test_download_mp3(settings):
    # Test downloading a video
    download_mp3(settings.youtube_urls[0], 0, settings)
    link_title = "Rick Astley - Never Gonna Give You Up (Official Music Video)"
    # Check that the mp3 file was created in the destination folder
    assert os.path.exists(f"{settings.destination}/{settings.prefix}{link_title}.mp3")
    # Clean up the downloaded file
    os.remove(f"{settings.destination}/")

    # Test handling of exceptions
    invalid_link = "invalid link"
    with pytest.raises(Exception):
        download_mp3(invalid_link, 0)
