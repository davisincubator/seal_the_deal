import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
from skimage import measure
import os
import numpy as np

def fishskin(i, show, sens):
    img = Image.open(i)
    img_gray = img.convert('L')
    contours = measure.find_contours(img_gray, sens)
    contours_long = list()
    for x in range (0, len(contours)):
        if len(contours[x]) > 99:
            contours_long.append(contours[x])
    if show:
        fig, ax = plt.subplots()
        ax.imshow(img, interpolation='nearest', cmap=plt.cm.gray)

        for n, contour in enumerate(contours_long):
            ax.plot(contour[:, 1], contour[:, 0], linewidth=1)
        ax.axis('image')
        ax.set_xticks([])
        ax.set_yticks([])
        plt.show()
    return(contours_long)