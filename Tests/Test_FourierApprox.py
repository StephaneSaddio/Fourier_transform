import sys
sys.path.append("..")
from src.Imgmanip import Imagemanip
from src.Class_fourierApproximation import FourierApprox
import unittest

class TestFourierApprox(unittest.TestCase):
    def test_FourierApprox_is_instance_of_FourierApprox(self):
        url = 'https://www.seekpng.com/png/detail/116-1164659_line-drawing-bunny-rabbit-at-getdrawings-bunny-drawing.png'
        Img = Imagemanip(url)
        Img.contours_search()
        Img.get_splines()

        xFT =  FourierApprox(Img.x_spl, (0, Img.num_pixels), num_circles= 50)
        self.assertIsInstance(xFT, FourierApprox)


if __name__=='__main__' : 
    unittest.main() 
