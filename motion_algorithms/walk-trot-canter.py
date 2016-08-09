import sys

# walk= 0 trot= 1 canter=2
current = 0
current_sec = 0
first_line = True
base_time = 0.0

walking = 0
troting = 0
cantering = 0

for line in sys.stdin:
	split = line.rstrip().split(' ')
	# print float(split[0])

	if first_line == True:
		prev_z = float(split[3])
		prev_sec = float(split[0])
		base_time = prev_sec
		first_line = False

	current_z = float(split[3])
	current_sec = float(split[0])

	current_z = float(split[3])
	current_sec = float(split[0])


	# if negative g force skip
	# if current_z < 16384.0:
	if current_z > 16384.0:
		print "first if"
		prev_z = current
		prev_sec = current_sec
		base_time = current_sec
		continue

	# check that number is still going up
	if prev_z < current_z:
		print "second if"
		prev_z = current_z
		prev_sec = current_sec
		continue


	# get top value by checking if the value has started to fall
	# if at this point our current is SMALLER than prev, prev is top of the motion curve
	if prev_z > 8192:
		print "third if"
		motion = 0
		# how much time has passed 
		walking += (base_time - current_sec)


print walking

