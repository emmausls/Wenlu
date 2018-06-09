#coding:utf-8

'''
from flask import Flask, jsonify
from flask_restful import Api

# init service and api
service = Flask(__name__)
api = Api(service)
'''

from flask import jsonify
from Services import service,api

# service status check
@service.route('/',methods=['GET'])
def status():
    return jsonify({'status':1})

# regeiste apis
from Services.Apis.user import User
api.add_resource(User,'/user/')


# start service
if __name__=='__main__':
    service.run(port=8000,debug=True)