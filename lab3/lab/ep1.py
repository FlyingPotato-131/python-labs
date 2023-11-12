import numpy as np
from PIL import Image
import os

if not os.path.exists('./edited_images'):
	os.makedirs('./edited_images')
for file in os.listdir('./lunar_images'):
	image = np.array(Image.open('./lunar_images/' + file), dtype = 'i')
	dark = np.min(image)
	bright = np.max(image)
	with np.nditer(image, op_flags = ['readwrite']) as it:
		for pixel in it:
			pixel[...] = 255 / (bright - dark) * (pixel - dark)
	Image.fromarray(image).convert('RGB').save('./edited_images/edited_{}'.format(file))
