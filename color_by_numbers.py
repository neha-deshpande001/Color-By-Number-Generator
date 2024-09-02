import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
import os
import random
import sys

def display_img_opencv_resize_first(img, img_name, new_max_dim=900):
    """
    We can resize the image before displaying it.  This is good
    for thumbnails.
    """
    max_dim = max(img.shape)
    scale = new_max_dim / max_dim
    new_height = int(img.shape[0] * scale)
    new_width = int(img.shape[1] * scale)
    img_1 = cv2.resize(img, (new_width, new_height))
    name_to_display = 'Resized ' + img_name
    cv2.imshow(name_to_display, img_1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if len(sys.argv) != 2:
    print("Usage: %s img\n" % sys.argv[0])
    print("where img is the input image")
    sys.exit()
else:
    img_name = sys.argv[1]

img_bgr = cv2.imread(img_name)
display_img_opencv_resize_first(img_bgr, "img_bgr")

img_white = np.ones(img_bgr.shape, dtype = np.uint8) * 255

# convert image to hsv
img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)


class Color:
    def __init__(self, name, max_hsv, min_hsv):
        self.name = name
        self.min_color = np.array(min_hsv,np.uint8)
        self.max_color = np.array(max_hsv,np.uint8)
        self.avg_color = np.array(np.add(min_hsv,max_hsv)/2,np.uint8)
        self.used = False
        self.id = 0

# color ranges from https://stackoverflow.com/a/66269158
colors = [
        Color('red1', [180, 255, 255], [159, 50, 70]),
        Color('red2', [9, 255, 255], [0, 50, 70]),
        Color('orange', [24, 255, 255], [10, 50, 70]),
        Color('yellow', [35, 255, 255], [25, 50, 70]),
        Color('green', [89, 255, 255], [36, 50, 70]),
        Color('blue', [128, 255, 255], [90, 50, 70]),
        Color('purple', [158, 255, 255], [129, 50, 70]),
        Color('black', [180, 255, 30], [0, 0, 0]),
        Color('gray', [180, 18, 230], [0, 0, 40]),
        Color('white', [180, 18, 255], [0, 0, 231])
    ]

# identify shapes and assign a color
num_colors_used = 0
for color in colors:
    mask = cv2.inRange(img_hsv, color.min_color, color.max_color)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #replace with RETR_TREE
    if len(contours) > 0:
        num_colors_used += 1
        color.used = True
        color.id = num_colors_used

    for contour in contours:
        # compute the center of the contour from https://pyimagesearch.com/2016/02/01/opencv-center-of-contour/
        M = cv2.moments(contour)
        if M['m00'] == 0.0:
            continue
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

        # draw the contour and center of the shape on the image
        cv2.drawContours(img_white, [contour], -1, (0, 0, 0), 2)

        if mask[cY,cX] == 255:
            cv2.putText(img_white, str(color.id), (cX-5, cY+5), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 0), 2) # this breaks if center of shape is a diff color


def convert_point_color(point, conversion):
    return cv2.cvtColor(np.uint8([[point]]), conversion)[0][0].tolist()

# create key
key = np.ones((img_white.shape[0],int(img_white.shape[1]*0.1),img_white.shape[2])).astype(np.uint8) * 255

# scale the key based on size of image
space_y = int(key.shape[1] * 0.2)
space_x = int(key.shape[0] / (num_colors_used + 2))
counter = int(space_x * 1.5)
cv2.putText(key, "KEY", (space_y, space_y*2), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

for color in colors:
    if color.used:
        cv2.rectangle(key, (space_y, counter+space_y), (space_y*2, counter), convert_point_color(color.avg_color,cv2.COLOR_HSV2BGR), -1) 
        cv2.rectangle(key, (space_y, counter+space_y), (space_y*2, counter), (0,0,0), 2) 
        cv2.putText(key, str(color.id), (space_y*3, int(counter+space_y/1.3)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
        counter += space_x


img_with_key = np.concatenate((img_white, key), axis=1)

# display image
display_img_opencv_resize_first(img_with_key, "img_with_key")
cv2.imwrite("final.png", img_with_key)


# some instances where the key doesn't work:
# - the calculated center of the shape is not in the shape or inside a different shape
# - a shape has an outline - the outline will look thick but the key will not display