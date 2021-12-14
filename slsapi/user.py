import logging
import json 
from flask import Flask, jsonify, make_response, request, session
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import pymysql
from MySqlDBManager import MySQLDBMgr as SqlDb

app = Flask(__name__)
api = Api(app)

def setup_logger():
        # create logger
        logger = logging.getLogger('project')
        logger.setLevel(logging.DEBUG)

        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        logger.addHandler(ch)

class Users(Resource):

    @app.route('/user/', methods=['GET'], endpoint='getall')
    def getall():        
        dbc = SqlDb.createDBConnection("MYSQL")
        rows = SqlDb.GetAllUsers(dbc)
        # data = []
        # for row in rows:
        #     data.append(list(row))
        return make_response(json.dumps(rows, indent = 2), 200)  # return data and 200 OK code
    pass

    @app.route('/user/<string:email>/', methods=['GET'], endpoint='getuser')
    def getUser(email):        
        dbc = SqlDb.createDBConnection("MYSQL")
        row = SqlDb.GetUserByEmail(dbc, email)
        return make_response(json.dumps(row, indent = 2), 200)  # return data and 200 OK code
    pass

    @app.route('/user/<string:email>/', methods=['DELETE'], endpoint='delete')
    def delete(email):
        try:       
            dbc = SqlDb.createDBConnection("MYSQL")
            count = SqlDb.deleteUser(dbc, email)
            if count == 1:
                return make_response('User deleted!', 200)  # return data and 200 OK code
            else:
                return make_response('Unable to delete user.', 500)
        except pymysql.ProgrammingError as err:
            return make_response('Failed deleting user!', 501)
            pass
    pass

    @app.route('/user/', methods=['POST'], endpoint='save')
    def save():
        count: int = -1
        if request.method == 'POST':
            try:
                email = request.form['email']
                firstname = request.form['firstname'] 
                lastname = request.form['lastname']
                if 'password' in request.form.keys():
                    password = request.form['password'] 
                dbc = SqlDb.createDBConnection("MYSQL")
                row = SqlDb.GetUserByEmail(dbc, email)
                count: int = -1
                if row == None:
                    dbc = SqlDb.createDBConnection("MYSQL")
                    count = SqlDb.addUser(dbc, firstname, lastname, email, password)
                    if count == 1:
                        return make_response('User added successfully!', 200)  # return data and 200 OK code
                    else:
                        return make_response('Failure, unable to add user!', 500)
                else:
                    dbc = SqlDb.createDBConnection("MYSQL")
                    count = SqlDb.updateUser(dbc, firstname, lastname, email)
                    if count == 1:
                        return make_response('User updated successfully!', 200)  # return data and 200 OK code
                    else:
                        return make_response('Failure, unable to update user!', 500)
               
            except pymysql.ProgrammingError as err:
                return make_response('Failed adding user!', 501, err)
                pass
    pass

if __name__ == '__main__' and __package__ is None:
  setup_logger()
  app.run()  # run our Flask app
  app.run(host='0.0.0.0', port=105)