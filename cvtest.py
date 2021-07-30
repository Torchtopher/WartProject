import cv2 as cv2
import numpy as np

image = cv2.imread(r"C:\Users\choll\AppData\Roaming\.minecraft\screenshots\rmsky.png")
hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

# Define lower and uppper limits of what we call "brown"
brown_lo=np.array([185, 210, 250])
brown_hi=np.array([195, 220, 255])

# Mask image to only select browns
mask=cv2.inRange(hsv,brown_lo,brown_hi)

# Change image to red where we found brown
image[mask>0]=(0,0,255)

cv2.imwrite("result.png",image)

cv2.imwrite("result.png",image)
cv2.imshow("Original", image)
cv2.waitKey(10000)
