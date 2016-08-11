# ms, xAccl, yAccl, zAccl, xGyro, yGyro, zGyro

import sys

for line in sys.stdin:
    line_array = line.split(' ')

    secs = float(line_array[0])
    y_accl = float(line_array[2]) / -16384.0

    print('%f %f' % (secs, y_accl))