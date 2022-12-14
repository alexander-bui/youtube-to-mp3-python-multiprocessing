# youtube_to_mp3_python_multiprocessing
Download Video in MP3 format using PyTube.
Ability to down to download multiple videos and playlists. Coded with multiprocessing for faster processing.

## Prequesites
Need to install Python 3. Recommended latest Python 3.

## How to use
1. (Optional): Create a virtual environment
2. Run `pip install -r requirements.txt`
3. Add youtube links to `youtube_urls` and  change destination folder in `destination`
4. Adjust `PROCESS_TYPE` and `NUMBER_OF_WORKERS` to preference
5. Run `python3 main.py` or `python main.py`

## Example Output
```
2022-12-14 17:47:57,562 [INFO] Downloading videos
2022-12-14 17:47:58,030 [INFO] Downloading Bella Donna.
2022-12-14 17:47:58,157 [INFO] Downloading Blade Runner.
2022-12-14 17:48:23,935 [INFO] Blade Runner has been successfully downloaded.
2022-12-14 17:48:24,351 [INFO] Bella Donna has been successfully downloaded.
2022-12-14 17:48:24,352 [INFO] Finished downloading videos
```