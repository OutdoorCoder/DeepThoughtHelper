import subprocess
import logging
from random import randint
from time import sleep
import deep_thought_helper

from is_now_in_time_period import is_now_in_time_period


def main():
    logging.basicConfig(filename='calls.log',
                        level=logging.INFO,
                        format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')

    while True:

        #if time is between 10pm and 11am, then run the program
        if is_now_in_time_period():

            logging.info("")
            deep_thought_helper.main()

            sleep(randint(1,20))

if __name__ == "__main__":
    main()
