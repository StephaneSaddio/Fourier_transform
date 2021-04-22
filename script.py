from FourierDrawing.ImageManipulation.Imgmanip import Imagemanip

url = 'https://www.seekpng.com/png/detail/116-1164659_line-drawing-bunny-rabbit-at-getdrawings-bunny-drawing.png'
img = Imagemanip(url)
img.show()

rabbit = Imagemanip(url)
rabbit.show()



rabbit.single_color()

rabbit.convert_binary(scale=3, thresh_val=200)

rabbit.thresh_val

rabbit.black_and_white()

rabbit.show_black_and_white()

rabbit.distance_matrix()

rabbit.contours_search(plot=True)

rabbit.get_splines(plot=True)
