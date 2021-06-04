import logging
import sys

a = 5
b = 0

try:
    c = a / b
except Exception as e:
    pass
    #logging.error("Wystapił wyjątek", exc_info=True)


sys.exit(0)

logger = logging.getLogger(__name__)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)
console_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_format)

file_handler = logging.FileHandler('plikloga.log')
file_handler.setLevel(logging.ERROR)
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_format)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.warning('To jest ostrzeżenie')
logger.error('To jest błąd')


sys.exit(0)
import logging.config

logging.config.fileConfig(fname='konfig.cfg', disable_existing_loggers=True)
nowy_logger = logging.getLogger("aaa")

nowy_logger.error('Nowy logger jest włączony')
logger.error('A to ciągle stary')