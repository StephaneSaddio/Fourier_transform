import sys
import unittest

sys.path.append('..')
from ImageManipulation.Imgmanip import Imagemanip

url = 'https://www.seekpng.com/png/detail/116-1164659_line-drawing-bunny-rabbit-at-getdrawings-bunny-drawing.png'

class test_Imgmanip(unittest.TestCase):

    def test_img_object (self):
        img = Imagemanip(url)
        self.assertIsInstance(img, Imagemanip)

    def test_thresh_val (self):
        img = Imagemanip(url)
        img.single_color()
        img.convert_binary(scale=3, thresh_val=200)
        self.assertGreater(img.thresh_val, 0) # thresh_val > 0
        self.assertLess(img.thresh_val, 255) # thresh_val < 255

    def convert_binary (self):
        """ """
        img = Imagemanip(url)
        img.single_color()
        img.convert_binary(scale=3, thresh_val=200)
        for i in range(len(img.image_array)):
            for j in range(len(img.image_array[0])):
                self.assertIn(img.image_array[i][j], (0,255))
        #self.assertIn(0, (8,255))

if __name__ == '__main__':
    unittest.main()

