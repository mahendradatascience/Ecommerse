# this config file for read the config.ini file.
#we can not read directly ini file 
import configparser

config=configparser.RawConfigParser()
config.read("E:/Software_Testing/PythonAutomationProgram/EcommerseProject/Configurations/config.ini") # .\\ mean current project directory EcommerseProject

class ReadConfig:
    @staticmethod
    def getApplicationURL(): # for every variable in ini file need to create a method
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        username=config.get('common info','useremail')
        return username

    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password
