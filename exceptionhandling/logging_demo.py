import logging

logging.basicConfig(filename="mylog.log", level = logging.DEBUG)
#log hierarchy below
logging.critical("Critical")
logging.error("Error")
logging.warning("Warn")
logging.debug("Debug")
logging.info("Info")

