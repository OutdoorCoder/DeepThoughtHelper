from datetime import datetime, time



timeStart = '4:00PM'
timeEnd = '12:00PM'
timeEnd = datetime.strptime(timeEnd, "%I:%M%p").time()
timeStart = datetime.strptime(timeStart, "%I:%M%p").time()
timeNow = datetime.now().time()

#print(timeStart)
#print(timeEnd)
#print(timeNow)

def isNowInTimePeriod():
    if timeStart < timeEnd:
        return timeNow >= timeStart and timeNow <= timeEnd
    else: #Over midnight
        return timeNow >= timeStart or timeNow <= timeEnd

#print(isNowInTimePeriod(timeStart, timeEnd, timeNow))
