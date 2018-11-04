from datetime import datetime, time

time_start = '1:00AM'
time_end = '12:00PM'
time_end = datetime.strptime(time_end, "%I:%M%p").time()
time_start = datetime.strptime(time_start, "%I:%M%p").time()
time_now = datetime.now().time()

#print(time_start)
#print(time_end)
#print(time_now)

def is_now_in_time_period():
    if time_start < time_end:
        return time_now >= time_start and time_now <= time_end
    else: #Over midnight
        return time_now >= time_start or time_now <= time_end

#print(is_now_in_time_period(time_start, time_end, time_now))
