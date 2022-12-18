# importing packages
from pytube import YouTube, Playlist
from moviepy.editor import AudioFileClip
import os
from multiprocessing import Pool
from functools import partial
import logging

PROCESS_TYPE = "PLAYLIST"  # CHOOSE PLAYLIST or URLS
NUMBER_OF_WORKERS = 4  # Declare num of core to use


logging.basicConfig(
    level=logging.INFO,  # INFO, ERROR
    format="%(asctime)s [%(levelname)s] %(message)s"
)


class Settings:
    youtube_urls = [
        "https://www.youtube.com/watch?v=ehThO11BJog",
        # "https://youtu.be/Zx7K5wUYRSI",
    ]  # add more if needed

    p = Playlist(
        'https://www.youtube.com/playlist?list=PL6ogdCG3tAWh4AShzQ-ThtBrooCutrNpM'
    )

    destination = "C:/Music"

    prefix = "Slipknot - "  # Set to "" for no prefix


def download_mp3(link, download_type, settings):
    try:
        # extract audio
        if download_type == 1:  # playlist
            logging.info(f'Downloading {link.title}.')
            audio = link.streams.get_audio_only()
        else:
            yt = YouTube(str(link))
            logging.info(f'Downloading {yt.title}.')
            audio = yt.streams.get_audio_only()

        # download the file
        out_file = audio.download(output_path=settings.destination)  # 128kbps

        # converts mp4 -> mp3 then saves the file. deletes mp4 file
        base, ext = os.path.splitext(out_file)
        ext2 = '.mp3'
        mp4_video = AudioFileClip(base+ext)
        mp4_video.write_audiofile(
            f"{settings.destination}\\{settings.prefix}{base[len(settings.destination)+1:]}{ext2}",
            bitrate="128k")
        mp4_video.close()
        os.remove(base+ext)

        # result of success
        if download_type == 1:  # playlist
            logging.info(f'{link.title} has been successfully downloaded.')
        else:
            logging.info(yt.title + " has been successfully downloaded.")
    except Exception as e:
        logging.error(f"error: {e}")


if __name__ == '__main__':
    pool = Pool(processes=NUMBER_OF_WORKERS)
    settings = Settings()
    try:
        # create all tasks
        logging.info("Downloading videos")
        if PROCESS_TYPE == "PLAYLIST":
            result = pool.map(partial(
                download_mp3, download_type=1, settings=settings),
                [link for link in settings.p.videos])
        else:
            result = pool.map(partial(
                download_mp3, download_type=0, settings=settings),
                [link for link in settings.youtube_urls])
        logging.info("Finished downloading videos")
    except KeyboardInterrupt:
        # User interrupt the program with ctrl+c
        logging.error("Exited via KeyboardInterrupt")
        pool.terminate()
        pool.join()
