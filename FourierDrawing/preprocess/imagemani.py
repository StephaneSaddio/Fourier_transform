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

    def convert_binary(self, scale=3, thresh_val=200):   

        # convert image to nympy array 
        image_array = np.array(image)

        # convert to binary image_array using thresh_val to cut
        white = 255
        black = 0

        initial_conv = np.where((image_array <= 200), image_array, white)
        final_conv = np.where((initial_conv > 200), initial_conv, black)
           
        image = Image.fromarray(image_array)
        
        # reduce number of non-zero pixels by scaling down the image
        self.img_scale = image.resize(tuple([int(v/scale) for v in image.size]),Image.ANTIALIAS)
    

    def black_and_white(self):
        
        # convert image to black and white
        self.img_blackwhite = self.img.convert(mode='1', dither=2)


#%%
rabbit = Imagemanip(img_raw)
rabbit.show()

