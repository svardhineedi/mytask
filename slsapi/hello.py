from random import randrange
from SqlDBManager import SQLDBMgr
from io import StringIO

def main():
    print("in main")
    try:
        dbc = SQLDBMgr.createDBConnection("DESKTOP-NSL7JSU\\SQLEXPRESS", "Demo", "sa", "Ma$t3rk3y")
        # dbc = SQLDBMgr.createDBConnection("(local)\\SQLEXPRESS", "Demo", "sa", "Ma$t3rk3y")
        irand = randrange(0, 10)
        uemail = f"user{irand}@myemail.com"
        fName = f"User{irand}"
        lName = f"last{irand}"
        pwd = f"pwd{irand}"
        rcount = SQLDBMgr.addUser(dbc, fName, lName, uemail, pwd)
        print(f"Inserted {rcount} row(s)")
    except Exception as ex:
        print("Error")

# Using the special variable 
# __name__
# if __name__=="__main__":
#     main()