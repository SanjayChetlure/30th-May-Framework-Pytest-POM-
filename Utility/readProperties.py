import configparser

config=configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class ReadConfig:

    @staticmethod
    def getAppURL():
        url=config.get("App Credentials","sauceLabURL")
        return url

    @staticmethod
    def getAppUN():
        un = config.get("App Credentials", "username")
        return un

    @staticmethod
    def getAppPWD():
        pwd = config.get("App Credentials", "password")
        return pwd

    #generic method
    @staticmethod
    def getINIFileData(sectionName,keyName):
        value = config.get(sectionName, keyName)
        return value