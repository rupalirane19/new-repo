import logging1

logging.basicConfig(filename = 'log1.txt',level =logging.warning)
message = 'logging'
logging.debug(message)
logging.info(message)
logging.warning(message)
logging.error(message)
logging.critical(message)