from typing import Text
from flask.json import jsonify
import pandas as pd
import pymysql
import logging
from contextlib import closing
log = logging.getLogger(__name__)
from config import DBConfig
from config import ConfigMgr

class DBMgr:

    # Create a SQL Server database connection. 
    def createDBConnection(config : DBConfig): 
        pass

    # Close the database connection 
    def closeDBConnection(connection): 
        pass 

    def GetAllUsers(connection: pymysql.Connection):
       pass 

    def GetUserByEmail(connection, email: Text):
        pass 

    def addUser(connection, firstname,lastname, email, password):
        pass  

    def updateUser(connection, newfirstname,newlastname, email):
        pass

    def deleteUser(connection, email):
       pass
