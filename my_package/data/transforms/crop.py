#Imports
import numpy as np


class CropImage(object):
    '''
        Performs either random cropping or center cropping.
    '''

    def __init__(self, shape, crop_type='center'):
        '''
            Arguments:
            shape: output shape of the crop (h, w)
            crop_type: center crop or random crop. Default: center
        '''
        self.shape = shape
        self.crop_type = crop_type
        # Write your code here

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''
        if self.crop_type == 'center':
            img_height, img_width = image.size
            return image.crop(((img_width - self.shape[1]) // 2, (img_height - self.shape[0]) // 2, (img_width + self.shape[1]) // 2, (img_height + self.shape[0]) // 2))
        else:
            assert image.shape[0] >= self.shape[0]
            assert image.shape[1] >= self.shape[1]
            x = np.random.randint(0, image.shape[1] - self.shape[1])
            y = np.random.randint(0, image.shape[0] - self.shape[0])
            a = image[y:y+self.shape[0], x:x+self.shape[1]]
            return a
        # Write your code here

        

 