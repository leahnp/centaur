# use data file to generate velocity data
# ms, xAccl, yAccl, zAccl, xGyro, yGyro, zGyro

# create new file for velocity data
# vel_file = open("mpu-1470608231100_rightside_velocity.dat", 'w')
vel_file = open("try.dat", 'w')


last_ms = 0
last_velocity = 0
first_line = True
velocity = 0

# with open("../data_lola/mpu-1470608231100.dat", "r") as data_file:
with open("../data_lola/mpu-1470608231117.dat", "r") as data_file:
    for line in data_file:
        line_array = line.split(' ')

        # if first line use ms as "last ms" and don't computer velocity
        if first_line == True:
            last_ms = int(line_array[0])
            first_ms = last_ms
            first_line = False
            continue

        # number on z acceleration when unit is not moving
        ms = int(line_array[0])
        zAccl = int(line_array[3])

        idk_what = 50
        lola_on_ground = zAccl > 0 & velocity < idk_what;

        if lola_on_ground == True:
            velocity = 0
        else: 
            delta_velocity = zAccl * (ms - last_ms) / 1000
            velocity = last_velocity + delta_velocity

        # print('%d %d' % (ms - first_ms, velocity))
        vel_file.write('%d %d\n' % (ms - first_ms, (-1* velocity)))

        last_ms = ms
        last_velocity = velocity

data_file.close()
vel_file.close()

# final_vel = initial_vel + (accelleration * time)

# v = lastv + (zaccel - gravity) * (ms - lastms)
# t in their equation is delta time, e.g. ms - lastms
