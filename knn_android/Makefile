#manuel - trim data to only have the name gait
#make - convert to seconds and trim out x,y 
#create features 
#feed into model and save model
#(turn knn.py into train and predict scripts)

#> type make, generate training data in the right form, 
#> type python predict.py and path, gen model and output reverse graph

# find all *.dat files in raw/
RAWDAT = $(wildcard raw/*.dat)

# convert filenames to reference training/ directory
TRAINDAT = $(subst raw/,training/,$(RAWDAT))
# new list equals sustituting all .dat from traindat with -feature1.dat
FEATURE1DAT = $(subst .dat,-feature1.dat,$(TRAINDAT))

FEATURE2DAT = $(subst .dat,-feature2.dat,$(TRAINDAT))

FEATUREDAT = $(FEATURE1DAT) $(FEATURE2DAT)

default: model/knn

# convert data from ms to seconds, trim x, y coordinates and pass argv of correct label
# 0 - stop/transition 1 - walk 2 - trot 3 - canter
training/walk-%.dat: raw/walk-%.dat
	python seconds_android.py 1 < $< > $@

training/trot-%.dat: raw/trot-%.dat
	python seconds_android.py 2 < $< > $@

training/canter-%.dat: raw/canter-%.dat
	python seconds_android.py 3 < $< > $@

# create feature1 
training/%-feature1.dat: training/%.dat feature1.py
	python feature1.py < $< > $@

# create feature2
training/%-feature2.dat: training/%.dat feature2.py
	python feature2.py < $< > $@



model/knn: $(FEATUREDAT)
	# echo $(FEATUREDAT)
	touch model/knn 

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


