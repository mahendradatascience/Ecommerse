# *** this is utilities file for logger configuration.
# this is one time for every test cases
import logging

class LogGen: 
    @staticmethod  # if method is static method then no need to create object for calling
    def loggen():  # we can directlye call without creating any object. also no need for  self key 
        logging.basicConfig(filename="E:\\Software_Testing\\PythonAutomationProgram\\EcommerseProject\\Logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
