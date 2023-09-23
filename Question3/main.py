#Amador UAVs - Question 3 - Nikhil Tamvada

#output in results\colordetect.out
#image proportions in images\analyze.png

from collections import Counter
from sklearn.cluster import KMeans
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
from color import colorconvert as cc
import cv2
image = cv2.imread('images\image2.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image)
def rgb_to_hex(rgb_color):
    hex_color = "#"
    for i in rgb_color:
        i = int(i)
        hex_color += ("{:02x}".format(i))
    return hex_color
def prep_image(raw_img):
    modified_img = cv2.resize(raw_img, (900, 600), interpolation = cv2.INTER_AREA)
    modified_img = modified_img.reshape(modified_img.shape[0]*modified_img.shape[1], 3)
    return modified_img
def color_analysis(img):
    with open ('colordetect.out', 'w') as out_file:
        clf = KMeans(n_clusters = 5)
        color_labels = clf.fit_predict(img)
        center_colors = clf.cluster_centers_
        counts = Counter(color_labels)
        ordered_colors = [center_colors[i] for i in counts.keys()]
        hex_colors = [rgb_to_hex(ordered_colors[i]) for i in counts.keys()]
        plt.figure(figsize = (12, 8))
        plt.pie(counts.values(), None, hex_colors, hex_colors)
        plt.savefig("images\\analyze.png")
        for elm in hex_colors:
             out_file.write("<"+ cc(elm) + "> ")
modified_image = prep_image(image)
color_analysis(modified_image)
