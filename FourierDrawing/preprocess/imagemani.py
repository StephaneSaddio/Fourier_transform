#%%

from PIL import Image
import requests
from io import BytesIO
import pylab
import numpy as np


#%%
url = 'https://www.seekpng.com/png/detail/116-1164659_line-drawing-bunny-rabbit-at-getdrawings-bunny-drawing.png'
response = requests.get(url)
img_raw = Image.open(BytesIO(response.content))
pylab.imshow(img_raw)
pylab.show()


#%%
class Imagemanip:

    def __init__(self, img_raw ):
    
    # Import raw image
        self.img = img_raw
        self.og_size = self.img.size
    
    def show(self):

    # Show raw image 
        imshow(np.asarray(self.img))

    def single_color(self):
        
        # convert image to single color 
        self.img_single_color = self.img.convert('L')

    def Binarize(self, scale=3, thresh_val=200):   
        
        # convert image to nympy array 
        image_array = np.array(image)

        # Binarize a numpy array using thresh_val as cutoff
        for i in range(len(image_array)):
            for j in range(len(image_array[0])):
                if image_array[i][j] > thresh_val:
                    image_array[i][j] = 255
                else:
                    image_array[i][j] = 0
        
        image = Image.fromarray(image_array)
        
        # scale image down to reduce number of non-zero pixels
        self.img_sm = image.resize(tuple([int(v/scale) for v in image.size]),Image.ANTIALIAS)
    

    def black_and_white(self):
        
        # convert image to black and white
        self.img_blackwhite = self.img.convert(mode='1', dither=2)


#%%

rabbit = Imagemanip(img_raw)
rabbit.show()




# %%
