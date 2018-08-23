import subprocess

from random import randint
from time import sleep

from isNowInTimePeriod import isNowInTimePeriod

while True:

    #if time is between like 11pm and 6am whatever time I'm in
    #TODO: Make this actually determine whether the code runs
    if isNowInTimePeriod():
        print(True)
    else:
        print(False)

    response = subprocess.run("python DeepThoughtHelper.py")

    print(response)

    if response.returncode == 1:
        print("Error has occured")
        break

    sleep(randint(10,40))
