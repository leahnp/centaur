#manual - trim data to only have the name gait
#make - convert to seconds and trim out x,y 
#create features 
#feed into model and save model
#(turn knn.py into train and predict scripts)

#> type make, generate training data in the right form, 
#> type python predict.py and path, gen model and output reverse graph

# find all *.dat files in raw/
RAWDAT = $(wildcard training_raw/*.dat)  $(wildcard predict_raw/*.dat)

PROCESSDAT = $(subst _raw,,$(RAWDAT))

# new list equals sustituting all .dat from traindat with -feature1.dat
FEATURE1DAT = $(subst .dat,-feature1.dat,$(PROCESSDAT))
FEATURE2DAT = $(subst .dat,-feature2.dat,$(PROCESSDAT))
FEATUREDAT = $(subst .dat,-features.dat,$(PROCESSDAT))

TRAINDAT = $(filter training/%,$(FEATUREDAT))
PREDICTDAT = $(filter predict/%,$(FEATUREDAT))

.PRECIOUS: $(FEATUREDAT) $(FEATURE1DAT) $(FEATURE2DAT)

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
# dat/feature1.dat: feature1.py dat/resample.dat
# 	python feature1.py < dat/resample.dat > dat/feature1.dat

# dat/feature2.dat: feature2.py dat/resample.dat
# 	python feature2.py < dat/resample.dat > dat/feature2.dat
#model/knn: $(TRAINDAT)
#	... generate knn model from training data ...
# look at https://www.gnu.org/software/make/manual/html_node/Automatic-Variables.html to 
# figure out how to get dependency file names



# default: dat/label.dat dat/feature1.dat dat/feature2.dat

# dat/seconds.dat: seconds.py canter-1359889.dat
# 	python seconds.py < dat/canter-1359889.dat > dat/seconds-canter-1359889.dat

# dat/resample.dat: resample.py dat/seconds-canter-1359889.dat
# 	python resample.py < dat/scale.dat > dat/resample.dat

# dat/label.dat: label.py dat/resample.dat
# 	python label.py < dat/resample.dat > dat/label.dat

# dat/feature1.dat: feature1.py dat/resample.dat
# 	python feature1.py < dat/resample.dat > dat/feature1.dat

# dat/feature2.dat: feature2.py dat/resample.dat
# 	python feature2.py < dat/resample.dat > dat/feature2.dat


