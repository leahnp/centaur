# use data file to generate velocity data

# create new file for velocity data
vel_file = open("velocity.dat", 'w')

with open("test_data.txt", "r") as data_file:
    for line in data_file:
    	# um, generate velocity
    	line_array = line.split(' ')
    	print line_array[0]
        # vel_file.write(velocity)

data_file.close()
vel_file.close()

# final_vel = initial_vel + (accelleration * time)

# v = lastv + (zaccel - gravity) * (ms - lastms)
# t in their equation is delta time, e.g. ms - lastms