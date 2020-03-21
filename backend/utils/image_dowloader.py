import requests
import shutil
import os
from flask import abort
from backend.utils.logger import logger


def download_img_from_url(url, file_name='img_tmp'):
    try:
        resp = requests.get(url, stream=True)
        resp.raise_for_status()
    except Exception as e:
        logger.error("Failed to download the image: %s", e)
        abort(400, {"error": "Failed to download the image"})

    with open(file_name, 'wb') as local_file:
        resp.raw.decode_content = True
        shutil.copyfileobj(resp.raw, local_file)

    path = os.getcwd() + '/' + file_name
    return path
