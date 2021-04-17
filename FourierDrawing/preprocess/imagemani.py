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

