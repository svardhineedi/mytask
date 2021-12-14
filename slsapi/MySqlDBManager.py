from typing import Text
from flask.json import jsonify
import pandas as pd
import pymysql
import pymysql.cursors
import logging
from contextlib import closing

from pymysql import cursors
from DBManager import DBMgr
from config import ConfigMgr, DBConfig
log = logging.getLogger(__name__)

class MySQLDBMgr(DBMgr):
    def __init__(self):
        pass

    # Create a MySQL database connection. 
    def createDBConnection(dbtype: str): 
        ''' 
        Take inputs server instance name, database name, username and password 
        Return a MySQL database connection 
        ''' 
        config:DBConfig = ConfigMgr.ReadConfig(dbtype)
        connection = pymysql.connect(host=config.host, 
                                        user=config.user, 
                                        password=config.password, 
                                        database=config.database, 
                                        port=int(config.port),
                                        cursorclass=pymysql.cursors.DictCursor)
        return connection 

    # Close the database connection 
    def closeDBConnection(connection): 
        '''Take input connection and close the database connection''' 
        try: 
            connection.close() 
        except pymysql.ProgrammingError: 
            pass 

    def GetAllUsers(connection: pymysql.Connection):
        query = "SELECT email, firstname, lastname from users"
        with closing(connection) as connection:
            with closing(connection.cursor()) as cursor:
                # cursor = connection.cursor() 
                try: 
                    cursor.execute(query)
                    rows = cursor.fetchall()
                    return rows
                except pymysql.DatabaseError: 
                    pass 

    def GetUserByEmail(connection, email: Text):
        query = "SELECT email, firstname, lastname from users WHERE email = %s"
        with closing(connection) as connection:
            with closing(connection.cursor()) as cursor:
                # cursor = connection.cursor()
                try: 
                    cursor.execute(query, (email,))
                    row = cursor.fetchone()
                    if row != None:
                        log.debug(f'GetUserByEmail is called with row %s',row)
                        print(f'GetUserByEmail is called with row %s', row)
                        return row
                    else:
                        log.debug(f'GetUserByEmail - user not found')
                        return None
                except pymysql.DatabaseError: 
                    pass 

    def addUser(connection, firstname,lastname, email, password):
        print('addUser is called')
        query = "INSERT INTO users (email, firstname, lastname, password) VALUES (%s, %s, %s,%s)"
        count: int = -1
        with closing(connection) as connection:
            with closing(connection.cursor()) as cursor:
                try: 
                    print('addUser execute query')
                    count = cursor.execute(query, (email, firstname, lastname, password))
                    log.debug(f'addUser is called with row count {count}')
                    connection.commit()
                    print(f'addUser2 is called with row count {count}')
                    return count
                except pymysql.DatabaseError as err:
                    log.debug('addUser error')
                    print(err.__cause__)
                    connection.rollback()    

    def updateUser(connection, newfirstname,newlastname, email):
        print(f'updateUser is called')
        query = "UPDATE users SET firstname = %s, lastname = %s WHERE email = %s"
        count: int = -1
        with closing(connection) as connection:
            with closing(connection.cursor()) as cursor:
                try: 
                    print(f'updateUser query executing')
                    count = cursor.execute(query, (newfirstname, newlastname, email))
                    print(f'updateUser is called with row count {count}')
                    connection.commit()
                    log.debug(f'updateUser is called with row count {count}')
                    return count
                except pymysql.DatabaseError as err:
                    connection.rollback()

    def deleteUser(connection, email):
        print(f'Delete user')
        query = "DELETE FROM users WHERE email = %s"
        count: int = -1
        with closing(connection) as connection:
            connection:pymysql.Connection
            with closing(connection.cursor()) as cursor:
                try:
                    print(f'deleteUser execute query')
                    count = cursor.execute(query, (email,))
                    connection.commit()
                    return count
                except pymysql.DatabaseError as err:
                    connection.rollback()
