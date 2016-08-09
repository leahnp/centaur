first_line = True
count = 0

with open("../data_lola/mpu-1470608231117.dat", "r") as data_file:
    for line in data_file:
        line_array = line.split(' ')

        if first_line == True:
            last_ms = int(line_array[0])
            first_ms = last_ms
            first_line = False
            continue

        if int(line_array[0]) - last_ms > 100:
        	count += 1
        	last_ms = int(line_array[0]) 
        	# print "ouch"


data_file.close()
print count