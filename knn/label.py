import sys

LABEL_UNDEFINED = 0
LABEL_WALK = 1
LABEL_TROT = 2
LABEL_CANTER = 3
 
for line in sys.stdin:
  split = line.split(' ')
  time = float(split[0])
  accel = float(split[1])

  if (time < 61.5):
    label = LABEL_WALK
  elif (time < 123.0):
    label = LABEL_TROT
  elif (time < 161.0):
    label = LABEL_CANTER
  elif (time < 174.0):
    label = LABEL_TROT
  else:
    label = LABEL_UNDEFINED

  print('%f %f %d' % (time, accel, label))

