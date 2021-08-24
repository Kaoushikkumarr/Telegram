from flask import Flask
from flask_cors import CORS
from flask_restful import Api

app = Flask(__name__)
CORS(app)
api = Api(app)

from routes import route

# Telegram API Signatures
api.add_resource(route.CollaborationAPI, '/this_is_test_api_for_collaborate')
api.add_resource(route.TelegramAPI, '/telegram')
