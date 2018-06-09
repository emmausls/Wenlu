# The services provide basicly restful api based on flask-restful for business
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

# definite app
service = Flask(__name__)

# definite api
api = Api(service)

# definite db models
service.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:{password}@47.106.81.197:3306/wl?charset=utf8mb4".format(password="nideshengrI@123")
db = SQLAlchemy(service)