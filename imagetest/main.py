from PIL import Image
import numpy as np
from random import randint

# Load the Image
img = Image.open("corgi.jpg")

def roll_pixel(p):
  return (p[1], p[2], p[0])

def mess_with_pixels(p):
  return ((p[0] + 10 ) % 256, p[1] + 20 % 256, p[2] + 30 % 256)

# this gets the pixel data 
pixels = iter(img.getdata())
width, height = img.size
print(width, height)

data = []
x = 0
for h in range(height - x):
  row = []
  for w in range(width + x):
    random = randint(0,3)
    if random == 1:
       pixel = next(pixels)
       row.append(pixel)
    elif random == 2:
       pixel = mess_with_pixels(next(pixels))
       row.append(pixel)
    else:
       p0 = randint(0, 255)
       p1 = 50
       p2 = randint(0, 255)
       pixel = (p0,p1,p2)
       row.append(pixel)
  data += [row]

def roll_picture(data):
  height, width = len(data), len(data[0])
  new_data = [[ (0,0,0) for j in range(height) ] for i in range(width)]
  for i in range(height):
    for j in range(width):
      new_data[j][i] = data[i][j]
  return new_data


def image_from_pixel_list(data):
  im = Image.fromarray(np.array(data, dtype=np.uint8))
  return im

# convert image 
im = image_from_pixel_list(data)
im.save("test.jpg")

roll_im = image_from_pixel_list(roll_picture(data))
roll_im.save("roll.jpg")


