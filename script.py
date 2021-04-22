from src.Imgmanip import Imagemanip
from src.Class_fourierApproximation import FourierApprox

url = 'https://www.seekpng.com/png/detail/116-1164659_line-drawing-bunny-rabbit-at-getdrawings-bunny-drawing.png'
Img = Imagemanip(url)

Img.single_color()
Img.convert_binary(scale=3, thresh_val=200)
Img.black_and_white()
Img.show_black_and_white()
Img.distance_matrix()
Img.contours_search()
Img.get_splines()


xFT =  FourierApprox(Img.x_spl, (0, Img.num_pixels), num_circles= 50)