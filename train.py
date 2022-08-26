import cv2 as cv
import glob
import numpy as np

folders = ["boats","fall", "canoe", "fountain01","fountain02","overpass"]
gap = 30

cnt = 0
def medi(inp,out,mask,Median_cal):
	linp = []
	lout = []
	a=1
	b=Median_cal
	for i in range(a, b, gap):
		tinp = cv.imread(inp[i])
		tout = cv.imread(out[i])
		tinp = np.asarray(tinp)
		tout = np.asarray(tout)
		linp.append(tinp)
		lout.append(tout)

	linp = np.asarray(linp)
	lout = np.asarray(lout)
	linp = np.minimum(linp, mask)
	lout = np.minimum(lout, mask)
	inp_med = np.median(linp ,axis = 0)
	return inp_med

for folder in folders:
	inp = glob.glob(folder +"\\input\\*jpg")
	out = glob.glob(folder +"\\groundtruth\\*png")
	mask = cv.imread(folder +'\\ROI.bmp')
	mask = np.asarray(mask)

	fp = open(folder +"\\temporalROI.txt", "r")
	a, b = str.split(fp.readline(), " ")
	a = int(a)
	Median_cal=a
	b = int(b)
	t=int((b-a+1)/2)
	b=a+t
	print("a= ",a," b= ",b)
	fp.close()

	linp = []
	lout = []
	for i in range(a, b, gap):
		tinp = cv.imread(inp[i])
		tout = cv.imread(out[i])
		tinp = np.asarray(tinp)
		tout = np.asarray(tout)
		linp.append(tinp)
		lout.append(tout)

	linp = np.asarray(linp)
	lout = np.asarray(lout)
	print(folder)
	linp = np.minimum(linp, mask)
	lout = np.minimum(lout, mask)
	inp_med = medi(inp,out,mask,Median_cal)
	#inp_med = np.median(linp ,axis = 0)
	cv.imwrite("train_med\\" +str(cnt) + ".jpg",inp_med)
	print(inp_med.shape)

	rinp = linp
	rout = lout

	for i in range(len(rinp)):
		res = np.concatenate((rout[i],rinp[i],inp_med),axis = 1)
		cv.imwrite("train\\" +str(cnt) + ".jpg",res)
		cnt = cnt + 1
