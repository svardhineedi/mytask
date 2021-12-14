import json
import logging
from dataclasses import dataclass

@dataclass
class DBConfig:
    host: str
    database: str
    port:str
    user: str
    password: str
    driver:str

class ConfigMgr:

    def ReadConfig(dbType)  -> DBConfig:
        print("Reading Config Json file...")
        jsonFile = open("Config/dbconf.json", "rb") # Open the JSON file for reading
        dbConfig = json.load(jsonFile) # Read the JSON into the buffer
        dbCon = dbConfig[dbType]
        print(dbCon)
        try:
            conf = DBConfig(dbCon["host"], dbCon["database"], dbCon["port"], dbCon["user"], dbCon["password"], dbCon["driver"])
            return conf
            #Object = lambda **kwargs: type("Object", (), kwargs)()
            #connectionConf = Object(host = dbCon["host"], user = "male", password = 42, database ="", port ="")
        except Exception as exc:
            print("Reading Config Json file - An error occurred !")
            logging.error(exc)
        finally:
            jsonFile.close() # Close the JSON file