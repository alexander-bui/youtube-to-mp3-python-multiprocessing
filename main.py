# importing packages
from pytube import YouTube, Playlist
from moviepy.editor import AudioFileClip
import os
from multiprocessing import Pool
from functools import partial

PROCESS_TYPE = "PLAYLIST" # CHOOSE PLAYLIST or URLS
NUMBER_OF_WORKERS = 4 # Declare num of core to use

import logging
logging.basicConfig(
    level=logging.INFO, # INFO, ERROR
    format="%(asctime)s [%(levelname)s] %(message)s"
)

youtube_urls = [
    "https://youtu.be/gVixaG76Ldg",
    "https://youtu.be/Zx7K5wUYRSI",
] # add more if needed

p = Playlist('https://www.youtube.com/playlist?list=PLR2DXFclGc0ahI8jEB-nHDjo8zAtqvpc4')

destination = "C:/Music"

def download_mp3(link,download_type):
    try:
        # extract audio
        if download_type == 1: # playlist
            logging.info(f'Downloading {link.title}.')
            audio = link.streams.get_audio_only()
        else:
            yt = YouTube(str(link))
            logging.info(f'Downloading {yt.title}.')
            audio = yt.streams.get_audio_only()
            
        # download the file
        out_file = audio.download(output_path=destination) # 128kbps
            
        # converts mp4 -> mp3 then saves the file. deletes mp4 file
        base, ext = os.path.splitext(out_file)
        ext2 = '.mp3'
        mp4_video = AudioFileClip(base+ext)
        mp4_video.write_audiofile(base+ext2)
        mp4_video.close()
        os.remove(base+ext)
            
        # result of success
        if download_type == 1: # playlist
            logging.info(f'{link.title} has been successfully downloaded.')
        else:
            logging.info(yt.title + " has been successfully downloaded.")
    except Exception as e:
        logging.error(f"error: {e}")


if __name__ == '__main__':
    pool = Pool(processes=NUMBER_OF_WORKERS)
    try:
        # create all tasks
        logging.info(f"Downloading videos")
        if PROCESS_TYPE == "PLAYLIST":
            result = pool.map(partial(download_mp3, download_type=1), [link for link in p.videos])
        else:
            result = pool.map(partial(download_mp3, download_type=0), [link for link in youtube_urls])
        logging.info(f"Finished downloading videos")
    except KeyboardInterrupt:
        # User interrupt the program with ctrl+c
        logging.error(f"Exited via KeyboardInterrupt")
        pool.terminate()
        pool.join()