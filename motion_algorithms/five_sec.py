# ondevicemotion node server to recieve data 
# jqery post wtc data
# save in var

import sys


interval_time = 0.0
average_array = []

for line in sys.stdin:
	#for each line, split on space
  split = line.split(' ')
  #take z accel value, normalize for gravity
  accel = (float(split[3]) / -16384.0) + 1.0
  #get current time
  time = float(split[0])
  #add accel to array
  average_array.append(accel)

  #check it time has reached specified interval
  if time >= (interval_time + 5.0):
  	#make var for number of values in array
  	values = len(average_array)
  	#take the sum of all values in array
  	accel_sum = sum(average_array)
  	#calculate the average
  	average = accel_sum/values
  	#print to file, with current time interval
  	print('%f %f' % (time, average)) 
  	#incerment time interval
  	interval_time += 5.0
  	#clear array
  	average_array = []
 