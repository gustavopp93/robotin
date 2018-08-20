from flask import Flask

from webapp import webhooks


app = Flask(__name__)

app.register_blueprint(webhooks.views.bp.bp, url_prefix='/webhooks')
