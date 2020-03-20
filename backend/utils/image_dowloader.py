import requests
import shutil
import os
from flask import abort
from backend.utils.logger import logger


def download_img_from_url(url, file_name='img_tmp'):
    try:
        resp = requests.get(url, stream=True)
    except Exception as e:
        logger.error("Failed to download the image: %s", e)
        abort(402, {"error": "Failed to download the image"})

    if resp.status_code == 400:
        logger.error("Failed to download the image: %s", resp.text)
        abort(400, {"error": resp.text})

    with open(file_name, 'wb') as local_file:
        resp.raw.decode_content = True
        shutil.copyfileobj(resp.raw, local_file)

    del resp
    path = os.getcwd() + '/' + file_name
    return path
