import sys

# walk= 0 trot= 1 canter=2
current = 0
current_sec = 0
first_line = True

walking = 0
troting = 0
cantering = 0

for line in sys.stdin:
	split = line.rstrip().split(' ')

	# secs = int(split[0])
	# z_accel = int(split[3])

	current = int(split[3])
	current_sec = int(split[0])

	if first_line == True:
		prev = int(split[3])
		prev_sec = int(split[0])
		first_line = False

	current = int(split[3])
	current_sec = int(split[0])


	# if negative g force skip
	if current < 16384.0:
		prev = current
		prev_sec = current_sec
		continue


	# get top value by checking if the value has started to fall
	if current > prev:
		prev = current
		prev_sec = current_sec
		continue

	# if at this point our current is SMALLER than prev, prev is top of the motion curve
	if prev < 8192:
		motion = 0

