import numpy as np
import imageio.v3 as img
import matplotlib.pyplot as plt

def zoomMinus(image, factor):
    height, width = image.shape[:2]
    new_height = int(height * factor)
    new_width = int(width * factor)
    imgZoom = np.zeros((new_height, new_width, 3), dtype=image.dtype)

    for y in range(new_height):
        for x in range(new_width):
            ori_y = int(y / factor)
            ori_x = int(x / factor)
            imgZoom[y, x] = image[ori_y, ori_x]

    return imgZoom

image = img.imread("C:\\Users\\dhika\\Documents\\singa.jpeg")
skala = 0.5  # Faktor untuk memperkecil gambar

imgZoom = zoomMinus(image, skala)

plt.subplot(1, 2, 1)
plt.imshow(image)

plt.subplot(1, 2, 2)
plt.imshow(imgZoom)
plt.show()
