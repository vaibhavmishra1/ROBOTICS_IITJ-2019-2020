import numpy as np
import cv2

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img, (0,0), (511, 511), (255, 255, 0), 5)
cv2.imshow('image', img)
cv2.waitKey(0)
img = cv2.rectangle(img, (230, 230), (270, 300), (0, 255, 0), 5)
cv2.imshow('image', img)
cv2.waitKey(0)
img = cv2.circle(img, (250, 265), 20, (0, 0, 255), -1)
cv2.imshow('image', img)
cv2.waitKey(0)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Learning OpenCV', (10, 500,), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()