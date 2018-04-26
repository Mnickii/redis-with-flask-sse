from flask import Flask
from own import StreamResource, publish
from flask_cors import CORS
from flask_restful import Api, Resource


app = Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost"

CORS(app)
api = Api(app)

class Send(Resource):
  def get(self):
    publish({"message": "Hello!"}, event_type='greeting', channel="channel1")
    return "Message sent!"

class Another(Resource):
  def get(self):
    publish({"message": "Wassup"}, event_type='hey', channel='channel2')
    return "Wassup yo!"


api.add_resource(StreamResource, '/stream')
api.add_resource(Send, '/send')
api.add_resource(Another, '/another')
