import subprocess
import logging
from random import randint
from time import sleep

from isNowInTimePeriod import isNowInTimePeriod


def main():
    logging.basicConfig(filename='calls.log',
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

            sleep(randint(1,3))

if __name__ == "__main__":
    main()
