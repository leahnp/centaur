# find all *.dat files in raw/
RAWDAT = $(wildcard training_raw/*.dat)  $(wildcard predict_raw/*.dat)

OUTDAT = $(subst _raw,,$(RAWDAT))
PROCESSDAT = $(subst .dat,-processed.dat,$(OUTDAT))
FEATURE1DAT = $(subst .dat,-feature1.dat,$(OUTDAT))
FEATURE2DAT = $(subst .dat,-feature2.dat,$(OUTDAT))
FEATURE3DAT = $(subst .dat,-feature3.dat,$(OUTDAT))
FEATUREDAT = $(subst .dat,-features.dat,$(OUTDAT))
PREDICTDAT = $(subst .dat,-predict.dat,$(filter predict/%,$(OUTDAT)))
PROBADAT = $(subst .dat,-proba.dat,$(filter predict/%,$(OUTDAT)))

FEATUREGRAPHS = $(subst .dat,.jpg,$(PROCESSDAT)) \
                $(subst .dat,.jpg,$(FEATURE1DAT)) \
                $(subst .dat,.jpg,$(FEATURE2DAT)) \
                $(subst .dat,.jpg,$(FEATURE3DAT))
PREDICTGRAPHS = $(subst .dat,.jpg,$(PREDICTDAT)) \
                $(subst .dat,.jpg,$(PROBADAT))

# preserve intermediate files so they are not removed after building
# final outputs
.PRECIOUS: $(PROCESSDAT) \
	       $(FEATURE1DAT) \
	       $(FEATURE2DAT) \
	       $(FEATURE3DAT) \
	       $(FEATUREDAT) \
	       $(PREDICTDAT) \
	       $(PROBADAT)

# default targets to build (e.g. when running `make` with no additional arguments)
default: $(FEATUREGRAPHS) $(PREDICTGRAPHS) model/knn

# process raw data into more desirable format (e.g. milliseconds to seconds)
training/walk-%-processed.dat: training_raw/walk-%.dat process.py
	python process.py 0 < $< > $@

training/trot-%-processed.dat: training_raw/trot-%.dat process.py
	python process.py 1 < $< > $@

training/canter-%-processed.dat: training_raw/canter-%.dat process.py
	python process.py 2 < $< > $@

predict/%-processed.dat: predict_raw/%.dat process.py
	python process.py 3 < $< > $@

%-feature1.dat: %-processed.dat feature1.py
	python feature1.py < $< > $@

%-feature2.dat: %-processed.dat feature2.py
	python feature2.py < $< > $@

%-feature3.dat: %-processed.dat feature3.py
	python feature3.py < $< > $@

# combine processed data with all features
%-features.dat: %-processed.dat %-feature1.dat %-feature2.dat %-feature3.dat
	paste -d ' ' $^ > $@

# training model
TRAINDAT = $(filter training/%,$(FEATUREDAT))
KNNMODEL = model/knn

$(KNNMODEL): $(TRAINDAT) train.py
	python train.py $(KNNMODEL) $(TRAINDAT)

# predict data
%-predict.dat: %-features.dat $(KNNMODEL) predict.py
	python predict.py $(KNNMODEL) < $< > $@

%-proba.dat: %-features.dat $(KNNMODEL) proba.py
	python proba.py $(KNNMODEL) < $< > $@

# generate graphs from features / predict data
%-processed.jpg: %-processed.dat
	echo "set terminal jpeg size 1024, 768 enhanced\n \
	plot '$<' using 1:2 title 'x-accel' with line lc rgb 'red', \
	     '$<' using 1:3 title 'y-accel' with line lc rgb 'green', \
	     '$<' using 1:4 title 'z-accel' with line lc rgb 'blue'" | gnuplot > $@

%-feature1.jpg: %-feature1.dat
	echo "set terminal jpeg size 1024, 768 enhanced\n \
	plot '$<' with line" | gnuplot > $@

%-feature2.jpg: %-feature2.dat
	echo "set terminal jpeg size 1024, 768 enhanced\n \
	plot '$<' with line" | gnuplot > $@

%-feature3.jpg: %-feature3.dat
	echo "set terminal jpeg size 1024, 768 enhanced\n \
	plot '$<' with line" | gnuplot > $@

%-predict.jpg: %-predict.dat
	echo "set terminal jpeg size 1024, 768 enhanced\n \
	set palette maxcolors 3\n \
	set palette defined (0 'red', 1 'green', 2 'blue')\n \
	set cbrange [0:3]\n \
	plot '$<' lt palette" | gnuplot > $@

%-proba.jpg: %-proba.dat
	echo "set terminal jpeg size 1024, 768 enhanced\n \
	plot '$<' using 1:2 title 'walk' with line lc rgb 'red', \
	     '$<' using 1:3 title 'trot' with line lc rgb 'green', \
	     '$<' using 1:4 title 'canter' with line lc rgb 'blue'" | gnuplot > $@