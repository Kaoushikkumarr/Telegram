from flask_restful import Resource
from controllers.telegram_connector import TelegramAPIController
from controllers.testing_controllers import Collaborations


class CollaborationAPI(Resource):
    def get(self):
        """ GET method for Collaboration API. """
        collaborate = Collaborations()
        result = collaborate.get_response_for_api()
        if result['response']:
            return result, 200
        elif result['status_code'] == 401:
            return result, 401
        return result, 202


class TelegramAPI(Resource):
    def get(self):
        """ GET method for Telegram API. """
        telegram = TelegramAPIController()
        result = telegram.get_telegram_api()
        if result:
            return {'response': result}, 200
        return {'response': result}, 202
