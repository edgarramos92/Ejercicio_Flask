#Snippet Codes for Python
#Video 17: Logging

import logging

format_log = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "prueba.log", level = logging.DEBUG, format = format_log, filemode = "w")
log = logging.getLogger()
log.info(' Log mesagge')
print (log.level)





