import sys
# importing android data as ms, x, y, z
# sys.argv[0] = script name "seconds_android.py"
# sys.argv[1] = label

first_line = True
first_ms = 0
label = sys.argv[1]

for line in sys.stdin:
    split = line.rstrip().split(' ')

    ms = float(split[0])

    if first_line == True:
        first_ms = ms
        first_line = False

    split[0] = str((ms - first_ms) / 1000.0);

    print('%s %s %s' % (split[0], split[3], label))

