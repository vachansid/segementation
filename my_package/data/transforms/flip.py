#Imports
import numpy as np


class FlipImage(object):
    '''
        Flips the image.
    '''

    def __init__(self, flip_type='horizontal'):
        '''
            Arguments:
            flip_type: 'horizontal' or 'vertical' Default: 'horizontal'
        '''
        self.flip_type = flip_type
        # Write your code here

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''
        a=np.copy(image)
        if self.flip_type == 'horizontal':
            np.flip(a, 0)
        else:
            np.flip(a, 1)
        return a
        # Write your code here

       