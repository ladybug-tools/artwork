"""This script resizes all images within emoji subfolders"""

import os
from PIL import Image

current_folder = os.path.dirname(os.path.realpath(__file__))
folder, scripts = os.path.split(current_folder)
icons_folder = 'icons_components'
plugins = ['ladybug', 'honeybee']
subfolder = 'emoji'

for plugin in plugins:
    directory = os.path.join(folder, icons_folder, plugin, subfolder)
    if os.path.isdir(directory):
        for img_file in os.listdir(directory):
            original_file = os.path.join(directory, img_file)
            with open(original_file, 'r+b') as f:
                with Image.open(f) as image:
                    img = image.resize((24, 24), Image.ANTIALIAS)
                    img.save(original_file)
