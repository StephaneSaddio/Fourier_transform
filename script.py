from Tests.src.Class_FourierApprox import Imagemanip
from Tests.src.Class_FourierApprox import FourierApprox

url = 'https://www.seekpng.com/png/detail/116-1164659_line-drawing-bunny-rabbit-at-getdrawings-bunny-drawing.png'
rabbit = Imagemanip(url)
rabbit.show()

rabbit.single_color()
rabbit.convert_binary(scale=3, thresh_val=200)
rabbit.black_and_white()
rabbit.show_black_and_white()
rabbit.distance_matrix()
rabbit.contours_search()
rabbit.get_splines()

xFT =  FourierApprox(rabbit.x_spl, (0, rabbit.length_pixels), num_circles= 50)

