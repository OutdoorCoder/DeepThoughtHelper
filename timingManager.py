import subprocess
import logging
from random import randint
from time import sleep

from isNowInTimePeriod import isNowInTimePeriod

logging.basicConfig(filename='records.log',
                    level=logging.INFO,
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

while True:

    #if time is between 10pm and 11am, then run the program
    if isNowInTimePeriod():

        response = subprocess.run("python DeepThoughtMain.py")

        logging.info(response)

        if response.returncode == 1:
            logging.error("Error has occured: %s", response)
            break

        sleep(randint(10,40))
