import imageio.v3 as iio
import numpy as np
from PIL import Image

filenames = ['Pic1.png', 'Pic.png']
images = []

# Get target size from the first image
first_image = Image.open(filenames[0])
target_size = first_image.size  # (width, height)

# Resize all images to the same size
for filename in filenames:
    img = Image.open(filename).resize(target_size)
    images.append(np.array(img))

# Save as gif
iio.imwrite('SM.gif', images, duration=500, loop=0)
