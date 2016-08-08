# use data file to generate velocity data
# ms, xAccl, yAccl, zAccl, xGyro, yGyro, zGyro

# create new file for velocity data
vel_file = open("velocity.dat", 'w')

last_ms = 0
last_velocity = 0
first_line = True

with open("test_data.txt", "r") as data_file:

    for line in data_file:
    	line_array = line.split(' ')

    	# if first line use ms as "last ms" and don't computer velocity
    	if first_line == True:
    		last_ms = int(line_array[0])
    		first_line = False
    		continue

    	# number on z acceleration when unit is not moving
    	gravity = 16000

    	ms = int(line_array[0])
    	zAccl = -int(line_array[3])

    	delta_velocity = (zAccl + gravity) * (ms - last_ms)
    	velocity = last_velocity + delta_velocity

    	vel_file.write(str(velocity) + '\n')
    	# print velocity

    	last_ms = ms
    	last_velocity = velocity

data_file.close()
vel_file.close()

# final_vel = initial_vel + (accelleration * time)

# v = lastv + (zaccel - gravity) * (ms - lastms)
# t in their equation is delta time, e.g. ms - lastms