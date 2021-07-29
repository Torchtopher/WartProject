import cv2
import numpy
import matplotlib


path = r'C:\Users\choll\AppData\Roaming\.minecraft\screenshots\photo.png'
img = cv2.imread(path)

window_name = 'photo'

cv2.imshow(window_name, img)

cv2.waitKey(0)

cv2.destroyAllWindows()