import cv2 as cv
import glob
import numpy as np

folder = "Shadow_res"

img = glob.glob(folder+"\\*jpg")
print(len(img))
pwc = 0
#update threshold here
th = 7

TP = 0
TN = 0
FP = 0
FN = 0
for i in img:
	t = cv.imread(i,0)
	h,w = t.shape
	w = w//2
	a = t[:,:w]
	b = t[:,w:]
	a = np.asarray(a)
	b = np.asarray(b)
	a[a>=th] = 255
	a[a<th]  = 0
	b[b>=th] = 254
	b[b<th]  = 1
	r = np.subtract(a,b)
	TP = TP + np.count_nonzero(r == 1)
	TN = TN + np.count_nonzero(r == -1)
	FP = FP + np.count_nonzero(r == -254)
	FN = FN + np.count_nonzero(r == 254)
if (TN+TP+FN+FP)!=0:
	pwc = (FP+FN)/(TN+TP+FN+FP)


print("PWC:",pwc)

