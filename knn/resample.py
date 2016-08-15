import sys

n = 10

sampled_time = 0.0
sampled_accel = 0.0
sampled = 0

for line in sys.stdin:
  split = line.split(' ')
  time = float(split[0])
  accel = float(split[1])

  sampled_time += time
  sampled_accel += accel
  sampled += 1

  if sampled >= n:
    print('%f %f' % (sampled_time / n, sampled_accel / n))
    sampled_time = 0.0
    sampled_accel = 0.0
    sampled = 0
