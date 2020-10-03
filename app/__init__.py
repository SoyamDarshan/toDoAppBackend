from pymongo import MongoClient
from flask import Flask
from flask_cors import CORS, cross_origin
import config

db = MongoClient(config.MONGO_URL)
db = db['to_do_db']

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    CORS(app)
    from app.to_do import bp as to_do_bp
    from app.authentication import bp as authentication_bp
    app.register_blueprint(to_do_bp)
    app.register_blueprint(authentication_bp)
    return app