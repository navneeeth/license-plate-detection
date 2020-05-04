#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 16:49:37 2020

@author: navneethkrishna
"""


from skimage import measure
from skimage.measure import regionprops
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import localization

# this gets all the connected regions and groups them together
i=0;
while(i<2):
    label_image = measure.label(localization.bins[i])
    
    # getting the maximum width, height and minimum width and height that a license plate can be
    plate_dimensions = (0.01*label_image.shape[0], 0.3*label_image.shape[0], 0.05*label_image.shape[1], 0.4*label_image.shape[1])
    min_height, max_height, min_width, max_width = plate_dimensions
    plate_objects_cordinates = []
    plate_like_objects = []
    fig, (ax1) = plt.subplots(1)
    ax1.imshow(localization.g[i], cmap="gray");
    
    # regionprops creates a list of properties of all the labelled regions
    for region in regionprops(label_image):
        if region.area <700:
            #if the region is so small then it's likely not a license plate
            continue
    
        # the bounding box coordinates
        min_row, min_col, max_row, max_col = region.bbox
        region_height = max_row - min_row
        region_width = max_col - min_col
        # ensuring that the region identified satisfies the condition of a typical license plate
        if region_height >= min_height and region_height <= max_height and region_width >= min_width and region_width <= max_width and region_width > region_height:
            plate_like_objects.append(localization.bins[i][min_row:max_row,
                                      min_col:max_col])
            plate_objects_cordinates.append((min_row, min_col,
                                                  max_row, max_col))
            rectBorder = patches.Rectangle((min_col, min_row), max_col-min_col, max_row-min_row, edgecolor="red", linewidth=2, fill=False)
            ax1.add_patch(rectBorder)
        # let's draw a red rectangle over those regions
    
    plt.show()
    i+=1
    
    
    
    
    
