'''
# Rectangular Kernel
>>> cv.getStructuringElement(cv.MORPH_RECT,(5,5))
array([[1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]], dtype=uint8)
# Elliptical Kernel
>>> cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
array([[0, 0, 1, 0, 0],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [0, 0, 1, 0, 0]], dtype=uint8)
# Cross-shaped Kernel
>>> cv.getStructuringElement(cv.MORPH_CROSS,(5,5))
array([[0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0],
       [1, 1, 1, 1, 1],
       [0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0]], dtype=uint8)
'''

import cv2 as cv
import glob
import numpy as np

folders = ["out"]
cnt = 0
kernel = np.ones((7,7),np.uint8)
for folder in folders:
    inp = glob.glob(folder+"\\*jpg")
    print(len(inp))
    linp = []
    for i in range(len(inp)):
        tinp = cv.imread(inp[i])
        if(i==1):
            print(type(tinp))
            print(tinp.shape)
        tinp = np.asarray(tinp)

        #res = cv.erode(tinp,kernel,iterations = 1)         #dec foreground
        #res = cv.dilate(tinp,kernel,iterations = 1)        #inc whiteness of foreground
        res = cv.morphologyEx(tinp, cv.MORPH_OPEN, kernel) #remove extra noise
        #res = cv.morphologyEx(tinp, cv.MORPH_CLOSE, kernel) #closing small holes inside the foreground
        #res = cv.morphologyEx(tinp, cv.MORPH_GRADIENT, kernel)


        
        res = cv.medianBlur(tinp, 9) # Add median filter to image
        res = cv.medianBlur(tinp, 5)
        
        
        #res = cv.bilateralFilter(tinp,9,75,75)

        #only blur
        #kernel = np.ones((5,5),np.float32)/25
        #res = cv.filter2D(tinp,-1,kernel)
        #res = cv.GaussianBlur(tinp,(5,5),0)
        #res = cv.blur(tinp,(5,5))
        compare = np.concatenate((tinp, res), axis=1)
        if(i==1):
            print(res.shape)
        linp.append(compare)

    linp = np.asarray(linp)

    for i in range(len(linp)):
        #res = np.concatenate((lout[i],linp[i],inp_med),axis = 1)
        cv.imwrite("after\\" +str(cnt) + ".jpg",linp[i])
        cnt = cnt + 1
        
