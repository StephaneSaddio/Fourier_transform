#%%
from PIL import Image
import requests
from io import BytesIO
import pylab
import numpy as np


#%%
url = 'https://www.seekpng.com/png/detail/116-1164659_line-drawing-bunny-rabbit-at-getdrawings-bunny-drawing.png'
#url = 'https://lh3.googleusercontent.com/proxy/_j7J9PlqYfCUUFduzzKbulOkZvdr526F88U481R5tV0eZGlNU2mNr-fURkUBseryy3aUIuc_x2uycYPcwE6QnQG05qdQ3E_5nEvlD0MF5M6zELEZa4CHIUjufmw-s_LoIdJO-Pk'
#url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Heraldique_chien_courrent.svg/1199px-Heraldique_chien_courrent.svg.png'


response = requests.get(url)
img_raw = Image.open(BytesIO(response.content))
print(img_raw.format,img_raw.size, img_raw.mode)
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
        # Show image informations
        print("The image format is : {}".format(self.img.format))
        print("The image size is : {}".format(self.img.size))
        print("The image mode is : {}".format(self.img.mode))
        
    def single_color(self):
        
        # convert image to single color
        self.img_single_color = self.img.convert('L')

    def convert_binary(self, scale=3, thresh_val=200):   

        # convert image to nympy array
        image_array = np.array(self.img_single_color)

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
        self.pixels = (1 - np.asarray(self.img_blackwhite).astype(int))
        self.pixels_line = np.reshape(self.pixels, self.pixels.size)

    def show_black_and_white(self):

        # Show black and white image 
        imshow(np.asarray(self.img_blackwhite))
        # Show black and white image informations
        print("The image format is : {}".format(self.img_blackwhite.format))
        print("The image size is : {}".format(self.img_blackwhite.size))
        print("The image mode is : {}".format(self.img_blackwhite.mode))
        print("Numbre of pixels is: {}".format(self.pixels.sum()))

    def distance_matrix(self):
    
        # Find positions of non-zero pixels
        non_zero_P_index = np.where(self.pixels_line > 0)[0]
        # Make a range array index form 1 to len(non_zero_P_index)
        arrange_index = np.array(range(1, len(non_zero_P_index)+1 ))
        
        # Replace each non-zero pixel with its number
        self.flat_img_mod = deepcopy(self.pixels_line)
        for rel, pix in enumerate(non_zero_P_index):
            self.flat_img_mod[pix] = rel+1

        # Get coordiantes for each non-zero pixel
        img_idx = np.reshape(self.flat_img_mod, self.pixels.shape)
        self.coord_list = []
        for p1 in arrange_index:
            p1_coords = tuple([int(c) for c in np.where(img_idx==p1)])
            self.coord_list.append(list(p1_coords))
        
        # Calcualte distance between each pair of coords
        self.distance_matrix = distance.cdist(self.coord_list, self.coord_list, 'euclidean')

    
#%%
rabbit = Imagemanip(img_raw)
rabbit.show()


#%%
rabbit.single_color()
rabbit.convert_binary(scale=3, thresh_val=200)
rabbit.black_and_white()
rabbit.show_black_and_white()
# %%
rabbit.distance_matrix()
# %%
