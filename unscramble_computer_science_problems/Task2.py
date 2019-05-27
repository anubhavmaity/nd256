"""
Read file into texts and calls.
It's ok if you don't understand how to read files
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
"""

telephone_duration_map = {}
for call in calls:
    caller = call[0]
    receiver = call[1]
    duration = int(call[3])
    if caller in telephone_duration_map:
        telephone_duration_map[caller] += duration
    else:
        telephone_duration_map[caller] = duration

    if receiver in telephone_duration_map:
        telephone_duration_map[receiver] += duration
    else:
        telephone_duration_map[receiver] = duration

telephone_number = max(telephone_duration_map, key=telephone_duration_map.get)
max_duration = telephone_duration_map[telephone_number]

print('{0} spent the longest time, {1} seconds, on the phone during September 2016.'.format(telephone_number, max_duration))
