import configparser

config = configparser.RawConfigParser()
config.read(r"F:\\job_project\\configuration\\config.ini")

class ReadConfigProperties:
    @staticmethod
    def get_url():
        url = config.get("common info","url")
        return url
    
    @staticmethod
    def get_username():
        username = config.get("common info","username")
        return username
    
    @staticmethod
    def get_password():
        password = config.get("common info","password")
        return password
