# feature 2 - mean beat length

import sys

WINDOW_LENGTH = 2.0

last_accel = None
last_time = None
window_data = []
window_total = 0.0

def push_data(time, beat):
  global window_data, window_total
  window_data.append({ 'time': time, 'beat': beat })
  window_total += beat

def pop_data():
  global window_data, window_total
  head = window_data.pop(0)
  window_total -= head['beat']

def expire_data(window_end):
  global window_data, window_total
  window_begin = window_end - WINDOW_LENGTH
  while 1:
    head = window_data[0]
    if (head['time'] > window_begin):
      break
    pop_data()

for line in sys.stdin:
  split = line.split(' ')
  time = float(split[0])
  accel = float(split[3])

  # check if the accel is crossing the x-axis 
  if last_accel and (last_accel >= 0.0) != (accel >= 0.0):
    if last_time:
      beat = (time - last_time)**0.5

      # push new data to the window
      push_data(time, beat)

      # expire old data from the window
      expire_data(time)

    # track last time the data crossed the x-axis
    last_time = time

  mean_beat = 0
  if len(window_data):
    mean_beat = window_total / len(window_data)
    
  print("%f %f" % (time, mean_beat))

  # track accel to see when the accel crosses the x-axis
  last_accel = accel
