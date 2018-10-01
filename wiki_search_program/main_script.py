import subprocess
import logging
from random import randint
from time import sleep

from is_now_in_time_period import is_now_in_time_period


def main():
    logging.basicConfig(filename='calls.log',
                        level=logging.INFO,
                        format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')

    while True:

        #if time is between 10pm and 11am, then run the program
        if is_now_in_time_period():

            response = subprocess.run("python deep_thought_helper.py")

            logging.info(response)

            if response.returncode == 1:
                logging.error("Error has occured: %s", response)
                break

            sleep(randint(1,3))

if __name__ == "__main__":
    main()
