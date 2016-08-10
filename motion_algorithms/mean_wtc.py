
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

	for line in sys.stdin:
		split = line.rstrip().split(' ')

		sec = float(split[0])
		x = float(split[1])  / 16384.0
		# start_sec =
		# start_secs = secs = float(split[0]) + 
		if start_sec_swap == False:
			t = time + (time * loops)
			# print t
			start_sec = sec + t
			loops += 1
			start_sec_swap = True

		# print sec
		# print start_sec

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
			print len(mean_list)
			mean_list = []
			start_sec_swap = False


average_gait(.005)
