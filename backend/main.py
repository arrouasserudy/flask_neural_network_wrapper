# Wrap a neural network model with Flask
# what you will do?
# - get an image as an input
# - run a neural network on it
# - return the results
# - wrap the app with docker with all relevant environment variables
#   the production start script should be named "serve"
# - except a /predict API call, add also /health API
# - eventually we want to call `docker run -p 8080:8080 image_name serve` and it will run the server

# things to take into consideration:
# logging
# virtualenv
# project folder structure
# use python3.6

from pathlib import Path
import click
import numpy as np
from keras.applications import ResNet50, imagenet_utils
from keras.preprocessing.image import img_to_array
from PIL import Image
from flask import abort
import os

from backend.utils.image_dowloader import download_img_from_url
from backend.utils.logger import logger

model = None


def prepare_image(image, target=(224, 224)):
    # if the image mode is not RGB, convert it
    if image.mode != "RGB":
        image = image.convert("RGB")

    # resize the input image and preprocess it
    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = imagenet_utils.preprocess_input(image)

    # return the processed image
    return image


def predict_image(image_path):
    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        logger.error("File not found %s", image_path)
        abort(500)

    prepared_image = prepare_image(image)
    image.close()
    os.remove(image_path)

    global model
    if not model:
        logger.info('Import ResNet50 model...')
        try:
            model = ResNet50(weights="imagenet")
        except Exception:
            logger.error("Failed to load the model")
            abort(500)
    logger.info('Predict...')
    preds = model.predict(prepared_image)
    return imagenet_utils.decode_predictions(preds)


def predict_handler(url):
    logger.info('Download image from: %s', url)

    image_path = download_img_from_url(url)
    predictions = predict_image(image_path)
    logger.info('Prediction: %s', predictions)
    return [[(t[0], t[1], t[2].item()) for t in prediction] for prediction in predictions]


@click.command()
@click.argument('image_path', type=Path)
def main(image_path):
    results = predict_image(image_path)
    print(results)


if __name__ == "__main__":
    main()
