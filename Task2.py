"""
Intro to Python Lab 1, Task 2

Complete each task in the file for that task. Submit the whole folder
as a zip file or GitHub repo. 
Full submission instructions are available on the Lab Preparation page.
"""

"""
Read file into texts and calls. 
It's ok if you don't understand how to read files
You will learn more about reading files in future lesson
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message: 
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.". 

HINT: Build a dictionary with telephone numbers as keys, and their
total time spent on the phone as the values. You might find it useful
to write a function that takes a key and a value and modifies a 
dictionary. If the key is already in the dictionary, add the value to
the key's existing value. If the key does not already appear in the
dictionary, add it and set its value to be the given value.
"""

def add_time(num, time):
    if num in num_time:
        num_time[num] += int(time)               # call[3] is string
    else:
        num_time[num] = int(time)
num_time = {}       # telephone_number : during_time
# get num_time dict from calls
for call in calls:
    add_time(call[0], call[3])
    add_time(call[1], call[3])
# get the max_time from num_time dict
max_time = 0
for num in num_time:
    if num_time[num] > max_time:
        max_time = num_time[num]
# get the corresponding numbers
for num in num_time:
    if num_time[num] == max_time:
        print("<" + num + "> spent the longest time, <" + str(max_time) + "> seconds, on the phone during September 2016.")



