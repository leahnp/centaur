import sys

first_line = True
first_ms = 0

for line in sys.stdin:
    split = line.rstrip().split(' ')

    ms = int(split[0])

    if first_line == True:
        first_ms = ms
        first_line = False

    split[0] = str((ms - first_ms) / 1000.0);

    print('%s %s %s %s %s %s %s' % (split[0], split[1], split[2], split[3], split[4], split[5], split[6]))

