
#%%
from PIL import Image
import requests
from io import BytesIO
import pylab

#%%
url = 'https://www.seekpng.com/png/detail/116-1164659_line-drawing-bunny-rabbit-at-getdrawings-bunny-drawing.png'
response = requests.get(url)
img = Image.open(BytesIO(response.content))
pylab.imshow(img)
pylab.show()


# %%

img = img.convert('L')
fig, ax = pylab.subplots()
contours = ax.contour(img, origin='image', levels=[100])
pylab.show()


# %%
