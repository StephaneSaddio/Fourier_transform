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

    def black_and_white(self):
        
        # convert image to black and white
        self.img_blackwhite = self.img.convert(mode='1', dither=2)

#%%

rabbit = Imagemanip(img_raw)
rabbit.show()




# %%
