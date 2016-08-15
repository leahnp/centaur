default: dat/label.dat dat/feature1.dat dat/feature2.dat

dat/seconds.dat: seconds.py dat/mpu-1470608231117.dat
	python seconds.py < dat/mpu-1470608231117.dat > dat/seconds.dat

dat/scale.dat: scale.py dat/seconds.dat
	python scale.py < dat/seconds.dat > dat/scale.dat

dat/resample.dat: resample.py dat/scale.dat
	python resample.py < dat/scale.dat > dat/resample.dat

dat/label.dat: label.py dat/resample.dat
	python label.py < dat/resample.dat > dat/label.dat

dat/feature1.dat: feature1.py dat/resample.dat
	python feature1.py < dat/resample.dat > dat/feature1.dat

dat/feature2.dat: feature2.py dat/resample.dat
	python feature2.py < dat/resample.dat > dat/feature2.dat
