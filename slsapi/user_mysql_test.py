import random
from random import randrange
import secrets
from datetime import datetime
from MySqlDBManager import MySQLDBMgr as mySqlDb

class TestMySqlClass:

    def test_getUser(self):        
        dbc = mySqlDb.createDBConnection("MYSQL")
        secretsGenerator = secrets.SystemRandom()
        irand = secretsGenerator.randrange(100000, 999999)
        uemail = f"user{irand}@myemail.com"
        fName = f"User{irand}"
        lName = f"last{irand}"
        pwd = f"pwd{irand}"
        count = mySqlDb.addUser(dbc, fName, lName, uemail,pwd)
        assert count == 1
        dbc = mySqlDb.createDBConnection("MYSQL")
        row = mySqlDb.GetUserByEmail(dbc, uemail)
        assert row["email"] == uemail and row["firstname"] == fName

    def test_create(self):
        dbc = mySqlDb.createDBConnection("MYSQL")
        secretsGenerator = secrets.SystemRandom()
        irand = secretsGenerator.randrange(100000, 999999)
        uemail = f"user{irand}@myemail.com"
        fName = f"User{irand}"
        lName = f"last{irand}"
        pwd = f"pwd{irand}"
        count = mySqlDb.addUser(dbc, fName, lName, uemail, pwd)
        assert count == 1

    def test_update(self):
        dbc = mySqlDb.createDBConnection("MYSQL")
        secretsGenerator = secrets.SystemRandom()
        irand = secretsGenerator.randrange(100000, 999999)
        uemail = f"user{irand}@myemail.com"
        fName = f"User{irand}"
        lName = f"last{irand}"
        pwd = f"pwd{irand}"
        count = mySqlDb.addUser(dbc, fName, lName, uemail, pwd)
        assert count == 1
        dbc = mySqlDb.createDBConnection("MYSQL")
        count = mySqlDb.updateUser(dbc, "upd_"+fName, "upd_"+lName, uemail)
        assert count == 1

    def test_delete(self):
        dbc = mySqlDb.createDBConnection("MYSQL")
        secretsGenerator = secrets.SystemRandom()
        irand = secretsGenerator.randrange(100000, 999999)
        uemail = f"user{irand}@myemail.com"
        fName = f"User{irand}"
        lName = f"last{irand}"
        pwd = f"pwd{irand}"
        count = mySqlDb.addUser(dbc, fName, lName, uemail,pwd)
        assert count == 1
        dbc = mySqlDb.createDBConnection("MYSQL")
        count = mySqlDb.deleteUser(dbc, uemail)
        assert count == 1