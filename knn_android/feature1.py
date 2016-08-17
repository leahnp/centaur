# feature 1 - z mean zacceleration

import sys

WINDOW_LENGTH = 5.0

window_data = []
window_total = 0.0

def push_data(time, zaccel):
  global window_data, window_total
  window_data.append({ 'time': time, 'zaccel': zaccel })
  window_total += zaccel

def pop_data():
  global window_data, window_total
  head = window_data.pop(0)
  window_total -= head['zaccel']

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
  zaccel = float(split[3])

  # push new data to the window
  push_data(time, zaccel)

  # expire old data from the window
  expire_data(time)

  mean_zaccel = window_total / len(window_data)
  print("%f %f" % (time, mean_zaccel))
