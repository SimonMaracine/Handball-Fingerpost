import sys
import logging

logging.basicConfig(filename="data\\__log.txt", format="\n%(asctime)s:%(levelname)s:%(message)s")


def exception_hook(exc_type, exc_value, exc_traceback):
    logging.error("Exception", exc_info=(exc_type, exc_value, exc_traceback))
    print("An error occurred: {}. Check the log file.".format(exc_value))


sys.excepthook = exception_hook
