import subprocess
from random import randint
from time import sleep
from isNowInTimePeriod import isNowInTimePeriod

while True:

    #if time is between like 11pm and 6am whatever time I'm in
    if isNowInTimePeriod():
        print(True)
    else:
        print(False)

    #run program
    response = subprocess.run("python DeepThoughtHelper.py")

    #TODO: get this to be a return code, and check if it's zero
    print(response)

    #wait randomized time
    sleep(randint(10,40))

    #if fails break
