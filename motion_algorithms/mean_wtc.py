for line in sys.stdin:
	split = line.rstrip().split(' ')

	secs = float(split[0])
	x = float(split[1])  / 16384.0


	# for 1 sec at a time, collect max and min values
	# add and divide to get mean
	# label gait accordingly


	# write to file with corresponding gait rgb value