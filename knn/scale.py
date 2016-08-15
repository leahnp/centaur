import sys

for line in sys.stdin:
  split = line.split(' ')
  time = float(split[0])
  accel = float(split[3])
  # MPU sensor outputs raw values of -32k / +32k for accel. the sensor's unit
  # of measurement was configured for -2 / +2 g's, scale it to this range
  accel /= -16384.0
  # offset for gravity
  accel += 1.0
  # normalize to -1.0 / +1.0
  accel = (accel / 2.0) * 1.0

  print('%f %f' % (time, accel))

