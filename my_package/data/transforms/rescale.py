#Imports
import numpy as np


class RescaleImage(object):
    '''
        Rescales the image to a given size.
    '''

    def __init__(self, output_size):
        '''
            Arguments:
            output_size (tuple or int): Desired output size. If tuple, output is
            matched to output_size. If int, smaller of image edges is matched
            to output_size keeping aspect ratio the same.
        '''
        self.output_size = output_size
        # Write your code here

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)

            Note: You do not need to resize the bounding boxes. ONLY RESIZE THE IMAGE.
        '''
        if isinstance(self.output_size, tuple):
            return image.resize(self.output_size)
        else:
            img_height, img_width = image.size
            if img_height > img_width:
                w = self.output_size
                h = w * (img_height/img_width)
                s = (w, h)
                return image.resize(s)
            else:
                x = self.output_size
                y = x * (img_width/img_height)
                z = (y, x)
                return image.resize(z)
        # Write your code here