import cv2
import matplotlib.pyplot as plt
import numpy as np

image_path = r"C:\Users\user\Pictures\erare\greyone.png"
image = cv2.imread(image_path)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray Image", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.hist(gray_image.ravel(),256,[0,255])
plt.show()

equalized_image = cv2.equalizeHist(gray_image)
cv2.imshow("Equalized Image", equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

_, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Binary Image", binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

low_pass_image = cv2.GaussianBlur(gray_image, (5,5), 0)
high_pass_image = cv2.subtract(gray_image, low_pass_image)
cv2.imshow("Low Pass Image", low_pass_image)
cv2.imshow("High Pass Image", high_pass_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=5)
sobel_image = cv2.bitwise_or(sobel_x, sobel_y)
canny_image = cv2.Canny(gray_image, 50, 150)
cv2.imshow("Sobel Image", sobel_image)
cv2.imshow("Canny Image", canny_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
