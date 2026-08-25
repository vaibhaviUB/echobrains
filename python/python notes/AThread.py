
'''
def function1():
    for i in range(5):
        print("hello")

def function2():
    for i in range(5):
        print("hi")

function1()
function2()
'''


























'''
#implementation of simple threads
import threading
import time
def display():
    for i in range(5):
        time.sleep(5)
        print("thread started")
        
t=threading.Thread(target=display())
'''

















#how to pass parameter in thread
'''
import threading
import time
def display(x,s,name):
    for i in range(x):
        time.sleep(s)
        print(name,"::started\n")
t=threading.Thread(target=display,args=(5,5,"THREAD1",))
t.start()
t1=threading.Thread(target=display,args=(5,4,"THREAD2",))
t1.start()
'''










#how to check thread is alive or not
'''
import threading
import time
def display(i):
    time.sleep(i)
        

t=threading.Thread(target=display,args=(4,),name="Thread#1",)
t.start()
t1=threading.Thread(target=display,args=(3,),name="Thread#2",)
t1.start()

for x in range(5):
    time.sleep(x+0.5)
    print('[',time.ctime(),t.name,t.is_alive(),']')
    print('[',time.ctime(),t1.name,t1.is_alive(),']')
'''

















#daemon thread
'''
import threading
import time
def worker_a():
    print("thread 1 started")
    time.sleep(5)
    print("thread 1 finished")
def worker_b():
    print("thread 2 started")
    print("thread 2 finished")

t1=threading.Thread(target=worker_a,daemon='true')
t1.start()
t2=threading.Thread(target=worker_b,)
t2.start()
'''










'''
t1.join()
t2.join()
'''













'''
import threading
import time

def worker():
    while True:
        print("Daemon thread is running")
        time.sleep(1)

# Create a daemon thread
t = threading.Thread(target=worker)
t.daemon = True  # Make the thread a daemon
t.start()

# Let the main program run for 5 seconds
time.sleep(5)
print("Main program is exiting, daemon thread will be killed.")
'''

























#Date and Time

#import the datetime module and display the current date:

'''
import datetime
x=datetime.datetime.now()# here now is function
print(x)
'''














'''In this example, the datetime.strptime()
function is used to convert the date strings to datetime objects, which can then be sorted.
You can then format them back to strings using strftime() if needed.'''






#Return the year and name of weekday:
'''
import datetime
x=datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

'''
#Create a date object:
'''
import datetime
x=datetime.datetime(2020,5,17)
print(x)
'''



#Display the name of the month:

'''
import datetime
x=datetime.datetime(2018,6,1)
print(x.strftime("%B"))
 '''   




#month formats

# import datetime
# x=datetime.datetime.now()
# print(x.strftime("%d"))#Day of month 01-31
# print(x.strftime("%b"))
# print(x.strftime("%B"))
# print(x.strftime("%m"))



#year formats

# import datetime

# x=datetime.datetime.now()

# print(x.strftime("%y"))
# print(x.strftime("%Y"))


#hourformat
'''
import datetime

x=datetime.datetime.now()

print(x.strftime("%H"))#Hour 00-23
print(x.strftime("%I"))#Hour 00-12
print(x.strftime("%p"))#am/pm
'''

#minutesformat
'''
import datetime

x=datetime.datetime.now()

print(x.strftime("%M"))#Minute 00-23
print(x.strftime("%S"))#Second 00-12
print(x.strftime("%f"))#Microsecond 000000-999999

'''


'''
import datetime

x=datetime.datetime.now()

print(x.strftime("%j"))#Day number of year 001-366
print(x.strftime("%U"))#Week number of year,Sunday as the first day of week, 00-52
print(x.strftime("%W"))#Week number of year,Monday as the first day of week, 00-53
print(x.strftime("%c"))#Local version of date and time
print(x.strftime("%x"))#Local version of date
print(x.strftime("%X"))#Local version of time

'''












#calender
'''
import calendar;
cal=calendar.month(2022,6)
#printing the calendar of December 2024
print(cal)
'''

















#Finding Duration Between Two Dates

'''
from datetime import datetime, timedelta

# Define two dates
date1 = datetime(2024, 10, 1)
date2 = datetime(2024, 10, 24)

# Calculate the difference
duration = date2 - date1

print(f"Duration: {duration}")
print(f"Days: {duration.days}")
'''









# Finding Duration Between Two Times
'''
from datetime import datetime, timedelta

# Define two times
time1 = datetime(2024, 10, 24, 8, 30, 0)  # 8:30 AM
time2 = datetime(2024, 10, 24, 17, 45, 0) # 5:45 PM

# Calculate the difference
duration = time2 - time1

# The result is a timedelta object
print(f"Duration: {duration}")
print(f"Total seconds: {duration.total_seconds()}")
'''









#Adding Duration to a Date
'''
from datetime import datetime, timedelta
# Adding 10 days to the current date
new_date = datetime.now() + timedelta(days=10)
print(f"New date: {new_date}")
'''







#Comparing Two Dates
'''
from datetime import datetime

# Define two dates
date1 = datetime(2024, 10, 1)
date2 = datetime(2024, 10, 24)

# Comparisons
print(f"Is date1 equal to date2? {date1 == date2}")
print(f"Is date1 not equal to date2? {date1 != date2}")
print(f"Is date1 earlier than date2? {date1 < date2}")
print(f"Is date1 later than date2? {date1 > date2}")
print(f"Is date1 earlier or equal to date2? {date1 <= date2}")
print(f"Is date1 later or equal to date2? {date1 >= date2}")
'''









#Example with conditional statements
'''
from datetime import datetime
date1 = datetime(2024, 10, 1)
date2 = datetime(2024, 10, 1)
if date1 < date2:
    print("date1 is earlier than date2.")
elif date1 > date2:
    print("date1 is later than date2.")
else:
    print("Both dates are the same.")
'''









#Sorting a List of Dates
'''
from datetime import datetime

# Create a list of dates
dates = [
    datetime(2024, 10, 5),
    datetime(2024, 9, 15),
    datetime(2024, 12, 25),
    datetime(2024, 7, 4)
]

# Sorting in ascending order
sorted_dates = sorted(dates)
print("Dates in ascending order:")
for date in sorted_dates:
    print(date)

# Sorting in descending order
sorted_dates_desc = sorted(dates, reverse=True)
print("\nDates in descending order:")
for date in sorted_dates_desc:
    print(date)


#Using sort() for In-Place Sorting

# Sorting in-place in ascending order
dates.sort()
print("\nIn-place sorted dates (ascending):")
for date in dates:
    print(date)

# Sorting in-place in descending order
dates.sort(reverse=True)
print("\nIn-place sorted dates (descending):")
for date in dates:
    print(date)

'''










#Sorting Dates as Strings

'''
from datetime import datetime

# List of date strings
date_strings = ["2024-10-05", "2024-09-15", "2024-12-25", "2024-07-04"]

# Convert to datetime objects
dates = [datetime.strptime(date, "%Y-%m-%d") for date in date_strings]

# Sort the dates
sorted_dates = sorted(dates)

print("\nSorted date strings as datetime objects:")
for date in sorted_dates:
    print(date.strftime("%Y-%m-%d"))


'''











#Stopping Execution Temporarily

'''
import time

print("This message will print immediately.")
time.sleep(5)  # Pause for 5 seconds
print("This message will print after a 5-second delay.")
'''



#Knowing The Time Taken By A Program
'''
import time

# Record the start time
start_time = time.time()

# The code block you want to measure
for i in range(1000000):
    pass  # Dummy loop for testing

# Record the end time
end_time = time.time()

"""
Measuring elapsed time allows developers to optimize code,
manage resources efficiently, benchmark algorithms, ensure real-time responsiveness,
debug and test effectively, and improve UX.
"""
# Calculate the elapsed time
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time:.6f} seconds")

'''












