#!/usr/local/bin/python3

import os
from PIL import Image

old_path = './images/'
new_path = './opt/icons/'

for image in os.listdir(old_path):
    print(image)
    if '.' not in image[0]:
        img = Image.open(old_path + image)
        new_filename = os.path.splitext(image)[0] + '.jpeg'  # Add .jpeg extension to the filename
        img.rotate(-90).resize((128, 128)).convert("RGB").save(os.path.join(new_path, new_filename), 'JPEG')
        img.close()