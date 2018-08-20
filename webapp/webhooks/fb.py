import json
import logging

import requests

from webapp import settings, constants


logger = logging.getLogger(__name__)


def get_sender(fb_sender_id):
    response = requests.get(
        "{}/{}".format(constants.FB_API_URI, fb_sender_id),
        params={"access_token": settings.FB_ACCESS_TOKEN}
    )
    return json.loads(response.content.decode("utf-8"))


def send_message(message):
    response = requests.post(
        "{}/me/messages".format(constants.FB_API_URI),
        params={"access_token": settings.FB_ACCESS_TOKEN},
        json=message
    )

    logger.info('Mensaje enviado')
