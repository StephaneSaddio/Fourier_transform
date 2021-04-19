#%%
from PIL import Image
import requests
from io import BytesIO
import pylab
import numpy as np

from copy import deepcopy
from scipy.spatial import distance
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
        #for i in range(len(image_array)):
        #    for j in range(len(image_array[0])):
        #        if image_array[i][j] > thresh_val:
        #            image_array[i][j] = 255
        #        else:
        #            image_array[i][j] = 0
        white = 255
        black = 0

        initial_conv = np.where((image_array > 200), image_array, 255)
        final_conv = np.where((initial_conv <= 200), initial_conv, 0)

        image = Image.fromarray(image_array)
        
        # reduce number of non-zero pixels by scaling down the image
        self.img_scale = image.resize(tuple([int(v/scale) for v in image.size]),Image.ANTIALIAS)
    
    def black_and_white(self):
        
        # convert image to black and white
        self.img_blackwhite = self.img_scale.convert(mode='1', dither=2)
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
    
        ## Get positions of non-zero pixels
        #absolute_index = np.where(self.pixels_line > 0)[0] 
        #relative_index = np.array(range(1, len(absolute_index)+1 ))
        #
        ## Replace each non-zero pixel in the array with its number
        ## i.e., the 10th non-zero pixel will have 10 in its place
        #self.flat_img_mod = deepcopy(self.pixels_line)
        #for rel, pix in enumerate(absolute_index):
        #    self.flat_img_mod[pix] = rel+1
#
        ## Get coordiantes for each non-zero pixel
        #img_idx = np.reshape(self.flat_img_mod, self.pixels.shape)
        #self.coord_list = []
        #for p1 in relative_index:
        #    p1_coords = tuple([int(c) for c in np.where(img_idx==p1)])
        #    self.coord_list.append(list(p1_coords))
        #
        ## Calcualte distance between each pair of coords
        #self.dist_mat = distance.cdist(self.coord_list, self.coord_list, 'euclidean')   

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

   
    def contours_search(self, plot=True):

        # Initialize search space with nearest neighbor tour

        edges = self.coord_list
        length_edges = len(edges)
        #....
        start = 1300
        # ...
        tour = [start]
        current_edge = start
        # ... 
        for step in range(0, length_edges):
            dist_row = deepcopy(self.distance_matrix[current_edge,:])
            for k in tour:
                dist_row[k] = np.inf
            nearest_neighbor = np.argmin(dist_row)
            if nearest_neighbor not in tour:
                tour.append(nearest_neighbor)
            current_edge = nearest_neighbor

        y_tour = -np.array([edges[tour[i % length_edges]] for i in range(length_edges+1) ])[:,0]
        y_tour = y_tour - y_tour[0]#- min(y_tour)
        x_tour = np.array([edges[tour[i % length_edges]] for i in range(length_edges+1) ])[:,1]    
        x_tour = x_tour - x_tour[0]#- min(x_tour)

        # Circle tour back to beginning
        np.append(x_tour, x_tour[0])
        np.append(y_tour, y_tour[0])
        length_edges = length_edges + 1
    
        self.x_tour = x_tour
        self.y_tour = y_tour
        self.length_pixels = length_edges

        if plot:
            plt.plot(self.x_tour, self.y_tour)
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

#%%
rabbit.contours_search(plot=True)
# %%

# %%
