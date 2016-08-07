# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# MPU-6000
# This code is designed to work with the MPU-6000_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Accelorometer?sku=MPU-6000_I2CS#tabs-0-product_tabset-2
import os
import smbus
import sys
import time
import uuid
from datetime import datetime
from datetime import timedelta

def millis_since_epoch():
	return int(time.time() * 1000)

# set up file to write to
filename = 'data/mpu-' + str(millis_since_epoch()) + '.dat'
output = open(filename, 'w')

# script, filename = argv, test.txt

# Get I2C bus
bus = smbus.SMBus(1)

# MPU-6000 address, 0x68(104)
# Select gyroscope configuration register, 0x1B(27)
#		0x18(24)	Full scale range = 2000 dps
bus.write_byte_data(0x68, 0x1B, 0x18)
# MPU-6000 address, 0x68(104)
# Select accelerometer configuration register, 0x1C(28)
#		0x18(24)	Full scale range = +/-16g
bus.write_byte_data(0x68, 0x1C, 0x18)
# MPU-6000 address, 0x68(104)
# Select power management register1, 0x6B(107)
#		0x01(01)	PLL with xGyro reference
bus.write_byte_data(0x68, 0x6B, 0x01)


#suspends exection x seconds
time.sleep(0.8)

# MPU-6000 address, 0x68(104)
# Read data back from 0x3B(59), 6 bytes
# Accelerometer X-Axis MSB, X-Axis LSB, Y-Axis MSB, Y-Axis LSB, Z-Axis MSB, Z-Axis LSB

# returns the elapsed milliseconds since the start of the program
start_time = datetime.now()

def millis_since_start():
	dt = datetime.now() - start_time
	ms = (dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0
	return ms

def readData():
	data = bus.read_i2c_block_data(0x68, 0x3B, 6)
	
	# Convert the data
	xAccl = data[0] * 256 + data[1]
	if xAccl > 32767 :
		xAccl -= 65536
	
	yAccl = data[2] * 256 + data[3]
	if yAccl > 32767 :
		yAccl -= 65536
	
	zAccl = data[4] * 256 + data[5]
	if zAccl > 32767 :
		zAccl -= 65536
	
	# MPU-6000 address, 0x68(104)
	# Read data back from 0x43(67), 6 bytes
	# Gyrometer X-Axis MSB, X-Axis LSB, Y-Axis MSB, Y-Axis LSB, Z-Axis MSB, Z-Axis LSB
	data = bus.read_i2c_block_data(0x68, 0x43, 6)
	
	# Convert the data
	xGyro = data[0] * 256 + data[1]
	if xGyro > 32767 :
		xGyro -= 65536
	
	yGyro = data[2] * 256 + data[3]
	if yGyro > 32767 :
		yGyro -= 65536
	
	zGyro = data[4] * 256 + data[5]
	if zGyro > 32767 :
		zGyro -= 65536

	# Save string data
	#x = "Acceleration in X-Axis : %d" %xAccl + "\n"
	#y = "Acceleration in Y-Axis : %d" %yAccl + "\n"
	#z = "Acceleration in Z-Axis : %d" %zAccl + "\n"
	#xr = "X-Axis of Rotation : %d" %xGyro + "\n"
	#yr = "Y-Axis of Rotation : %d" %yGyro + "\n"
	#zr = "Z-Axis of Rotation : %d" %zGyro + "\n"

	#writeFile(x, y, z, xr, yr, zr)
	writeFile(xAccl, yAccl, zAccl, xGyro, yGyro, zGyro)
	return
                                                

def getDiskSpace():
	    p = os.popen("df -h /")
	    i = 0
	    while 1:
	        i = i +1
	        line = p.readline()
	        if i==2:
	            return(line.split()[1:5])

# Disk information
DISK_stats = getDiskSpace()
DISK_total = DISK_stats[0]
DISK_free = DISK_stats[1]
DISK_perc = DISK_stats[3]

# write to file
def writeFile(xAccl, yAccl, zAccl, xGyro, yGyro, zGyro):
	ms = millis_since_start()
	output.write('%d %d %d %d %d %d %d\n' % (ms, xAccl, yAccl, zAccl, xGyro, yGyro, zGyro))
	return

count = 0
while (count < 1000):
	readData()
	count = count + 1

print "Done!"
print DISK_total
print DISK_free
print DISK_perc
print millis_since_start()

output.close()
