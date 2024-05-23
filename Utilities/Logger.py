# import logging
#
#
# class LogGenerator:
#     @staticmethod
#     def loggen():
#         logfile = logging.FileHandler("C:\\Users\\hp\\PycharmProjects\\nopCommerce_Project\\Logs\\nopCommerce.log")
#         format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s")
#         logfile.setFormatter(format)    # setting format to the logs
#         logger = logging.getLogger()    # to generate Log
#         logger.addHandler(logfile)      # adding log everytime to same file
#         logger.setLevel(logging.INFO)   # set log level
#         return logger


import logging
import inspect


class LogGenerator:
    @staticmethod
    def loggen():
        logname = inspect.stack()[1][3]  # runtime - getting filepath - class -method
        logger = logging.getLogger(logname)  # to generate Log
        logfile = logging.FileHandler("C:\\Users\\hp\\PycharmProjects\\nopCommerce_Project\\Logs\\nopCommerce.log")
        format = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s")
        logfile.setFormatter(format)  # setting format to the logs
        logger.addHandler(logfile)  # adding log everytime to same file
        logger.setLevel(logging.INFO)  # set log level
        return logger
