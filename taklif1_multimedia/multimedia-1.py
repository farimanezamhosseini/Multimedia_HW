import cv2
import numpy as np
from PIL import Image
#First part of the first question reading and displaying from a disk
image_path = r"C:\Users\user\Pictures\erare\color.png"
image = cv2.imread(image_path)
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Second part of the first question printing the information of the image 
image = Image.open(image_path)
print("File Name:", image.filename)
print("Format:", image.format)
print("Mode:", image.mode)
print("Size:", image.size)
print("Color Depth:", image.info.get('color depth'))


#Third part of the first question color image including three different channels r,g,b 
image_np = np.array(image)
b,g,r = cv2.split(image_np)
cv2.imshow("Red", r)
cv2.imshow("Green", g)
cv2.imshow("Blue", b)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Fourth part of the first question resizeing the image 50%
resized_img = cv2.resize(image_np, (0,0), fx=0.5, fy=0.5)
cv2.imshow("Resized Image", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Fifth part of the first question converting the image to grayscale
gray_img = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Sixth part of the first question converting the image to 16 colors
indexed_img = cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB)
cv2.imshow("Indexed Image", indexed_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Seventh part of the first question calculating the complement of the image
complement_img = 255 - image_np
cv2.imshow("Complement Image", complement_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Eighth part of the first question calculating the subtraction and the sum of the image and its complement
complement_img_color = cv2.cvtColor(complement_img, cv2.COLOR_BGR2RGB)
sum_img = image_np + complement_img
subtraction_img = image_np - complement_img
cv2.imshow("Subtraction Image", subtraction_img)
cv2.imshow("Sum Image", sum_img)
cv2.waitKey(0)
cv2.destroyAllWindows()






