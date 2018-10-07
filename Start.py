import os
import time
from datetime import datetime
from datetime import timedelta
import math

start_time = datetime(2018, 10, 10, 18, 20, 00) #Specify start date
now = datetime.now() #Specify current date 
time_current = now

while start_time > time_current: #Conditional operator
    

    time_gap = start_time - time_current #Difference between start date and current date
    time_gap_days = time_gap.days #Calculate integer number of days
    if time_gap_days >1: 
        adder_days = "дня" 
    else:
        adder_days = "день"
    time_gap_hours = math.floor(time_gap.seconds/3600) #Calculate integer number of hours
     

    time_gap_hours_def  = time_gap_hours - math.floor(time_gap_hours/10)*10 

    if time_gap_hours_def>=5 or time_gap_hours_def == 0 or (time_gap_hours>=11 and time_gap_hours <=14): 
        adder_hours = "часов"
    elif time_gap_hours_def >=2 and time_gap_hours_def < 5 :
        adder_hours = "часа"
    else:
        adder_hours = "час"
    

    time_gap_minutes = math.floor((time_gap.seconds - time_gap_hours*3600)/60) #Calculate integer number of minutes

    time_gap_minutes_def  = time_gap_minutes - math.floor(time_gap_minutes/10)*10
    if time_gap_minutes_def >= 5 or time_gap_minutes_def == 0 or (time_gap_minutes>=11 and time_gap_minutes <=14):
        adder_minutes = "минут"
    elif time_gap_minutes_def >=2 and time_gap_minutes_def < 5 :
        adder_minutes = "минуты"
    else:
        adder_minutes = "минута"
    
    time_gap_seconds = time_gap.seconds - time_gap_hours*3600 - time_gap_minutes*60 # Calculate integer number of seconds
    time_gap_seconds_def = time_gap_seconds - math.floor(time_gap_seconds/10)*10

    if time_gap_seconds_def >= 5 or time_gap_seconds_def == 0 or (time_gap_seconds>=11 and time_gap_seconds <=14) : 
        adder_seconds = "секунд"
    elif time_gap_seconds_def >=2 and time_gap_seconds_def < 5 :
        adder_seconds = "секунды"
    else:
        adder_seconds = "секунда"

    print("До начала курса осталось:", time_gap.days, adder_days, time_gap_hours, adder_hours, time_gap_minutes, adder_minutes, time_gap_seconds, adder_seconds)
    time_current = time_current+timedelta(seconds=1)
    time.sleep(1)
    os.system('cls')
    
