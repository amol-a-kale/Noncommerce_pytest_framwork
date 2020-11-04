import configparser
config=configparser.RawConfigParser()
config.read("configuration/config.ini")

class ReadConfig:
    @staticmethod
    def geturl():
        url=config.get('common info','baseurl')
        return url

    @staticmethod
    def getusername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getpassword():
        password= config.get('common info', 'password')
        return password