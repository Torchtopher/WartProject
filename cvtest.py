import cv2 as cv2
import numpy as np

image = cv2.imread(r"C:\Users\choll\AppData\Roaming\.minecraft\screenshots\rmsky.png")
hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

# Define lower and uppper limits of what we call "brown"
brown_lo=np.array([100, 20, 20])
brown_hi=np.array([110, 255, 255])
# Mask image to only select browns
mask=cv2.inRange(hsv,brown_lo,brown_hi)

# Change image to red where we found brown
image[mask>0]=(0,0,0)

cv2.imwrite("result.png",image)

cv2.imwrite("result.png",image)
cv2.imshow("Result", image)
cv2.waitKey(10000)
