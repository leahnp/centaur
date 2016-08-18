# feature 3 - mean normalized x-accel

import math
import sys

WINDOW_LENGTH = 2.0

window_data = []
window_total = 0.0

def push_data(time, xaccel):
  global window_data, window_total
  window_data.append({ 'time': time, 'xaccel': xaccel })
  window_total += xaccel

def pop_data():
  global window_data, window_total
  head = window_data.pop(0)
  window_total -= head['xaccel']

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
  accel = [float(split[1]), float(split[2]), float(split[3])]
  accel_len = math.sqrt(accel[0]*accel[0] + accel[1]*accel[1] + accel[2]*accel[2])
  accel_normalized = [accel[0] / accel_len, accel[1] / accel_len, accel[2] / accel_len]

  # push new data to the window
  push_data(time, accel_normalized[0])

  # expire old data from the window
  expire_data(time)

  mean_zaccel = window_total / len(window_data)
  print("%f %f" % (time, mean_zaccel))
