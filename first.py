import numpy as np
import cv2
import matplotlib.pyplot as plt

original_image = cv2.imread('image3.png')

# Filter by passing image through 3x3 averaging filter
average_image = cv2.blur(original_image, (3, 3))

# Apply 3x3 median filter on the original image
median_image = cv2.medianBlur(original_image, 5)
gaussian_image = cv2.GaussianBlur(original_image, (3, 3), 99)

plt.imshow(median_image, 'Greys')
plt.show()
