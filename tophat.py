import time
from PIL import ImageGrab, ImageChops

img = ImageGrab.grab(bbox=None)

while True:
	diff = ImageChops.difference(ImageGrab.grab(bbox=None), img)
	bbox = diff.getbbox()
	if bbox is not None:
		print ('\a')
		ImageChops.screen(ImageChops.invert(img.crop(bbox)), diff.crop(bbox)).show()
		time.sleep(5)
		img = ImageGrab.grab(bbox=None)
