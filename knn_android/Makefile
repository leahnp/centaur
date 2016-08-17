# find all *.dat files in raw/
RAWDAT = $(wildcard training_raw/*.dat)  $(wildcard predict_raw/*.dat)

# new list equals sustituting all .dat from traindat with -feature1.dat
OUTDAT = $(subst _raw,,$(RAWDAT))
PROCESSDAT = $(subst .dat,-processed.dat,$(OUTDAT))
FEATURE1DAT = $(subst .dat,-feature1.dat,$(OUTDAT))
FEATURE2DAT = $(subst .dat,-feature2.dat,$(OUTDAT))
FEATUREDAT = $(subst .dat,-features.dat,$(OUTDAT))

TRAINDAT = $(filter training/%,$(FEATUREDAT))
PREDICTDAT = $(filter predict/%,$(FEATUREDAT))

.PRECIOUS: $(PROCESSDAT) $(FEATURE1DAT) $(FEATURE2DAT) $(FEATUREDAT)

default: model/knn $(PREDICTDAT)

# convert data from ms to seconds, trim x, y coordinates and pass argv of correct label
# 0 - stop/transition 1 - walk 2 - trot 3 - canter
training/walk-%-processed.dat: training_raw/walk-%.dat seconds_android.py
	python seconds_android.py 1 < $< > $@

training/trot-%-processed.dat: training_raw/trot-%.dat seconds_android.py
	python seconds_android.py 2 < $< > $@

training/canter-%-processed.dat: training_raw/canter-%.dat seconds_android.py
	python seconds_android.py 3 < $< > $@

predict/%-processed.dat: predict_raw/%.dat seconds_android.py
	python seconds_android.py 5 < $< > $@

# create feature1 (for all directories)
%-feature1.dat: %-processed.dat feature1.py
	python feature1.py < $< > $@

# create feature2 (for all directories)
%-feature2.dat: %-processed.dat feature2.py
	python feature2.py < $< > $@

# create zipped features with space in between (sec, z-accel, label, mean accel, mean beat)
%-features.dat: %-processed.dat %-feature1.dat %-feature2.dat
	paste -d ' ' $^ > $@

# run train.py on features data
model/knn: $(TRAINDAT) train.py
	python train.py model/knn $(TRAINDAT)

# echo $(FEATURE1DAT)