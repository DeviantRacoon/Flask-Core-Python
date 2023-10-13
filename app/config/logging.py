import logging
from colorama import init, Fore

init(autoreset=True)
logging.basicConfig(level = logging.ERROR)

file_handler = logging.FileHandler('logs/error.log')
file_handler.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logging.getLogger('').addHandler(file_handler)

def logger(func):
    try:
        func()
    except Exception as err:
        logging.error(f"{Fore.RED}[-] Ha ocurrido un error: {err}")


