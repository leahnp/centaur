import sys

first = True
last_accel = 0.0
local_max = [0.0, 0.0]

for line in sys.stdin:
  split = line.split(' ')
  secs = float(split[0]) * 10.0
  accel = (int(split[3]) / -16384.0) + 1.0
 
  if not first and (last_accel >= 0.0) != (accel >= 0.0):
    print('%f %f' % (local_max[0], local_max[1]))
    first = True
    last_accel = 0.0
    local_max = [0.0, 0.0]
    continue

  first = False
  last_accel = accel
  if (accel >= 0.0 and accel >= local_max[1]):
    local_max[0] = secs
    local_max[1] = accel
  elif (accel < 0.0 and accel <= local_max[1]):
    local_max[0] = secs
    local_max[1] = accel













# import sys

# # def check_axis_swap(axis):
# # 	if axis == 'positive':
# # 		axis = 'negative'
# # 	else: 
# # 		axis = 'positive'
# # 	return axis

# #start MAX/MIN tracking when passes 16k
# axis = 'negative'
# swap = 0
# min = -.75
# min_sec = 0.0
# max = --.75
# max_sec = 0.0

# for line in sys.stdin:
# 	split = line.rstrip().split(' ')

# 	# z = float(split[3]) / -16384.0
# 	x = float(split[1])  / 16384.0

# 	# if z < min:
# 	# 	min = z
# 	# if z > max:
# 	# 	max = z


# 	# walk check
# 	# positive
# 	if (x >= 0.0) and (x < .75):
# 		# check_axis_swap(axis)
# 		if axis == 'negative':
# 			axis = 'positive'
# 			swap = True
# 		else: 
# 			swap = False

# 		if x > max:
# 			# print "hi"
# 			max = x
# 			max_sec = float(split[0])

# 		# print 'positive'

# 		if swap == True:
# 			# print max
# 			print('%f %f %d' % (max_sec, max, 1))
# 			max = 0.0
# 			max_sec = 0.0

# 	elif (x < 0.0) and (x > -.75):
# 		# check_axis_swap(axis)
# 		if axis == 'positive':
# 			axis = 'negative'
# 			swap = True
# 		else: 
# 			swap = False

# 		if x < min:
# 			# print "min hi"
# 			min = x
# 			min_sec = float(split[0])

# 		# print 'negative'

# 		if swap == True:
# 			# print min
# 			print('%f %f %d' % (min_sec, min, 1))
# 			min = 0.0
# 			min_sec = 0.0

# 	# else:
# 	# 	print('%s %s %d' % (split[0], x, 2))

# 	# trot check
# 	# how to know if data isnt walk or begining of trot/canter
# 	# positive
# 	if (x >= .75) and (x < 1.25):
# 		# check_axis_swap(axis)
# 		if axis == 'negative':
# 			axis = 'positive'
# 			swap = True
# 		else: 
# 			swap = False

# 		if x > max:
# 			# print "hi"
# 			max = x
# 			max_sec = float(split[0])

# 		# print 'positive'

# 		if swap == True:
# 			# print max
# 			print('%f %f %d' % (max_sec, max, 1.5))
# 			max = 0.0
# 			max_sec = 0.0

# 	elif (x <= -.75) and (x > -1.25):
# 		# check_axis_swap(axis)
# 		if axis == 'positive':
# 			axis = 'negative'
# 			swap = True
# 		else: 
# 			swap = False

# 		if x < min:
# 			# print "min hi"
# 			min = x
# 			min_sec = float(split[0])

# 		# print 'negative'

# 		if swap == True:
# 			# print min
# 			print('%f %f %d' % (min_sec, min, 1.5))
# 			min = 0.0
# 			min_sec = 0.0

# 	# else:
# 	# 	print('%s %s %d' % (split[0], x, 2))



# # print min, max





# # print walking


# # # walk= 0 trot= 1 canter=2
# # current = 0
# # current_sec = 0
# # first_line = True
# # base_time = 0.0

# # walking = 0
# # troting = 0
# # cantering = 0

# # for line in sys.stdin:
# # 	split = line.rstrip().split(' ')
# # 	# print float(split[0])

# # 	if first_line == True:
# # 		last_z = float(split[3])
# # 		# prev_sec = float(split[0])
# # 		last_time = float(split[0])
# # 		first_line = False

# # 	# current_z = float(split[3])
# # 	# current_sec = float(split[0])

# 	# if negative g force skip
# 	# if current_z < 16384.0:
# 	# if current_z > 16384.0:
# 	# 	print "first if"
# 	# 	prev_z = current
# 	# 	prev_sec = current_sec
# 	# 	base_time = current_sec
# 	# 	continue

# 	# # check that number is still going up
# 	# if prev_z < current_z:
# 	# 	print "second if"
# 	# 	prev_z = current_z
# 	# 	prev_sec = current_sec
# 	# 	continue


# 	# # get top value by checking if the value has started to fall
# 	# # if at this point our current is SMALLER than prev, prev is top of the motion curve
# 	# if prev_z > 8192:
# 	# 	print "third if"
# 	# 	motion = 0
# 	# 	# how much time has passed 
# 	# 	walking += (base_time - current_sec)
