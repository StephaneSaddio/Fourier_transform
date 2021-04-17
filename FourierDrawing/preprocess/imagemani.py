#%%
from PIL import Image
import requests
from io import BytesIO
import pylab
import numpy as np


#%%
url = 'https://www.seekpng.com/png/detail/116-1164659_line-drawing-bunny-rabbit-at-getdrawings-bunny-drawing.png'
response = requests.get(url)
img_brut = Image.open(BytesIO(response.content))
pylab.imshow(img_brut )
pylab.show()


#%%
class Imagemanip:

    def __init__(self, img_brut ):
        self.img = img_brut
        self.og_size = self.img.size
    
    def show(self):
        imshow(np.asarray(self.img))


#%%
rabbit = Imagemanip(img_brut)
rabbit.show()

# %%
