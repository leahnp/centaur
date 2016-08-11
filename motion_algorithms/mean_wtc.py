
import sys
	# for 1 sec at a time, collect max and min values
	# add and divide to get mean
	# label gait accordingly


	# write to file with corresponding gait rgb value

def average_gait(time):
	axis = 'negative'
	swap = 0
	min = 0
	min_sec = 0.0
	max = 0
	max_sec = 0.0
	mean_list = []
	start_sec_swap = False
	loops = 0
	# start_sec = 0

	for line in sys.stdin:
		split = line.rstrip().split(' ')

		sec = float(split[0])
		x = float(split[1])  / 16384.0
		start_sec = sec

		if start_sec_swap == False:
			start_sec = start_sec + time
			loops += 1
			start_sec_swap = True

		if sec < start_sec:
			if (x >= 0.0):
				# check_axis_swap(axis)
				if axis == 'negative':
					axis = 'positive'
					swap = True
				else: 
					swap = False

				if x > max:
					max = x
					max_sec = float(split[0])

				# print 'positive'

				if swap == True:
					# print max
					# print('%f %f %d' % (max_sec, max, 1))
					mean_list.append([max_sec, max])
					max = 0.0
					max_sec = 0.0

			elif (x < 0.0):
				# check_axis_swap(axis)
				if axis == 'positive':
					axis = 'negative'
					swap = True
				else: 
					swap = False

				if x < min:
					# print "min hi"
					min = x
					min_sec = float(split[0])

				if swap == True:
					# print min
					# print('%f %f %d' % (min_sec, min, 1))
					mean_list.append([min_sec, min])
					min = 0.0
					min_sec = 0.0

		else:
			# print mean_list
			if len(mean_list):
				print len(mean_list)
				# mean = get_mean(mean_list)
			# mean_list = []
			start_sec_swap = False


def get_mean(list):
	# print list
	max = []
	min = []
	for item in list:
		if item[1] > 0:
			max.append(item)
		else:
			min.append(item)
	# now I have 2 array min and max values, find mean
	grand_max = mean(max)
	grand_min = mean(min)

	# if grand_min == None:
	# 	continue
	# if grand_max == None:
	# 	continue

	# print grand_min
	# print grand_max

	# if (grand_max < .40):
	# 	print 'walk'

	# elif (grand_max < 1.25):
	# 	print 'trot'
	# else:
	# 	print 'canter'

	# if -.75 <= grand_max <= .75:
	# 	print 'walk' + str(grand_max)

	# if -.75 <= grand_min <= .75:
	# 	print 'walk' 

	# if .75 <= grand_max <= 1.25:
	# 	print 'trot'

	# if -.75 >= grand_min >= -1.25:
	# 	print 'trot'

	# if 1.25 <= grand_max:
	# 	print 'canter'

	# if -1.25 >= grand_min:
	# 	print 'canter'

def mean(list):
	print list
	s = 0
	items = len(list)
	if items == 0:
		return
	# REFACTOR: don't need secs at this point 
	for item in list:
		# print item[1]

		s = s + item[1]
	# print s
	if s == 0:
		return
	mean =  (s/items)
	print mean
	return mean




average_gait(.05)
