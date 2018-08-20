import json

from flask import request, Response
from werkzeug.exceptions import Forbidden

from webapp import settings, constants
from webapp.webhooks.fb import get_sender, send_message
from .bp import bp


@bp.route('/robotin', methods=["GET"])
def web_hook_get():
    """
    This handles facebook verification of our web hook
    """
    mode = request.args.get("hub.mode")
    verification_token = request.args.get("hub.verify_token")
    if mode == "subscribe" and verification_token == settings.FB_VERIFICATION_TOKEN:
        return Response(request.args.get("hub.challenge"), mimetype='application/json')
    raise Forbidden


@bp.route('/robotin', methods=["POST"])
def web_hook_post():
    """
    This handles messages from facebook messenger
    """
    data = json.loads(request.data.decode("utf-8"))
    if data['object'] == "page":
        for entry in data["entry"]:
            fb_page_id = entry["id"]
            _time = entry["time"]
            for event in entry["messaging"]:
                sender_id = event["sender"]["id"]
                sender = get_sender(sender_id)

                message = {
                    "recipient": {
                        "id": sender_id
                    },
                    "message": {
                        "text": 'Hola {first_name} {last_name}'.format(
                            first_name=sender['first_name'],
                            last_name=sender['last_name']
                        )
                    },
                    "messaging_type": constants.FB_MESSAGE_RESPONSE
                }
                send_message(message)
    return Response()
