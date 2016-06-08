import cv2
import math
import numpy as np

img1 = cv2.imread('img1.png')
img2 = cv2.imread('img2.png')
res = img2
mask = img2
diff = cv2.absdiff(img2, img1)

# cv2.imwrite('diff.png',diff)

rows, cols, channels = img1.shape

# compare each piexl with threhold
for i in range(0,rows):
	for j in range(0, cols):
		dist = math.sqrt(int(diff[i, j, 0])*int(diff[i, j, 0])+int(diff[i, j, 1])*int(diff[i, j, 1])+int(diff[i, j, 2])*int(diff[i, j, 2]))
		if dist < 50:
			mask[i,j] = [0,0,0]		

# cv2.imwrite('mask.png', mask)

# handle noise
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

