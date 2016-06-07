import cv2
import math

img1 = cv2.imread('img1.png')
img2 = cv2.imread('img2.png')
res = img2
mask = img2
diff = img2 - img1
cv2.imwrite('diff.png',diff)

rows, cols, channels = img1.shape

for i in range(0,rows):
	for j in range(0, cols):
		# dist = math.sqrt(int(diff[i, j, 0])*int(diff[i, j, 0])+int(diff[i, j, 1])*int(diff[i, j, 1])+int(diff[i, j, 2])*int(diff[i, j, 2]))
		if int(diff[i, j, 0]) < 1:
			mask[i,j] = [0,0,0]		
print diff[1,2]
cv2.imwrite('222.png', mask)

