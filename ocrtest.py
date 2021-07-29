import pytesseract
import cv2
import numpy as np
pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\choll\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"


# Read image
img = cv2.imread(r'C:\Users\choll\PycharmProjects\pythonProject\numberss.png')

# threshold red
lower = np.array([254, 254, 254])
upper = np.array([255, 255, 255])
thresh = cv2.inRange(img, lower, upper)



# save results
cv2.imwrite('wart_thresh.jpg', thresh)
text = pytesseract.image_to_string("wart_thresh.jpg", lang='mc')
numeric_filter = filter(str.isdigit, text)
text = "".join(numeric_filter)
print(text)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()