# Imports
from PIL import ImageDraw, Image, ImageFont
import numpy as np


def plot_visualisation(img, masks, bboxes, labels, output):  # Write the required arguments
    img = Image.fromarray(np.uint8(img.transpose((1, 2, 0)) * 255))
    for i in range(min(3, len(bboxes))):

        temp=img.load()
        d,height,width=masks[i].shape
        for y in range(height):
            for x in range(width):
                if((masks[i])[0][y][x] > 0.4):
                    r, g, b = temp[x ,y]
                    if i==0:
                        temp[x, y]= (r,0,0)
                    if i==1:
                        temp[x, y]= (0,b,0)
                    if i==2:
                        temp[x, y]= (0,0,g)

        ImageDraw.Draw(img).rectangle(bboxes[i], outline='blue', width=4)
        ImageDraw.Draw(img).text(bboxes[i][0], labels[i], fill='yellow')

    img.save(output)
# The function should plot the predicted boxes on the images and save them.
# Tip: keep the dimensions of the output image less than 800 to avoid RAM crashes.
