from PIL import Image, ImageFilter

orig = Image.open("hills.jpeg")
orig.load()

blured = orig.filter(ImageFilter.GaussianBlur(radius=0))
sharp = orig.filter(ImageFilter.UnsharpMask(radius=0))
median = orig.filter(ImageFilter.MedianFilter(1))

orig.show()
median.show()





