# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from skimage.io import imread
from skimage.filters import threshold_otsu
import matplotlib.pyplot as plt
from skimage.util import crop

im = imread("frame9.jpg", as_grey=True)
car_image = crop(im, ((500, 2200), (40, 900)), copy=False)
print(car_image.shape)
gray_car_image = car_image * 255
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(gray_car_image, cmap="gray")
threshold_image = threshold_otsu(gray_car_image)
binary_car_image = gray_car_image > threshold_image
ax2.imshow(binary_car_image, cmap="gray")
plt.show()

car_image1 = crop(im, ((400, 2000), (900, 200)), copy=False)
print(car_image1.shape)
gray_car_image1 = car_image1 * 255
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.imshow(gray_car_image1, cmap="gray")
threshold_image1 = threshold_otsu(gray_car_image1)
binary_car_image1 = gray_car_image1 > threshold_image1
ax2.imshow(binary_car_image1, cmap="gray")
plt.show()
bins= [binary_car_image,binary_car_image1]
g=[gray_car_image,gray_car_image1]


