"""This script strips out underscores from all component icon filen ames."""

import os

current_folder = os.path.dirname(os.path.realpath(__file__))
folder, scripts = os.path.split(current_folder)


subfolders = ['png', 'emoji']

for subdir in subfolders:
    bug_directory = os.path.join(folder, 'icons_bugs', subdir)
    for img_file in os.listdir(bug_directory):
        new_img_file = img_file.replace('_', '')
        original_file = os.path.join(bug_directory, img_file)
        new_file = os.path.join(bug_directory, new_img_file)
        os.rename(original_file, new_file)

icons_folder = 'icons_components'
plugins = ['ladybug', 'honeybee', 'dragonfly']
subfolders = ['png', 'emoji']

for plugin in plugins:
    for subdir in subfolders:
        directory = os.path.join(folder, icons_folder, plugin, subdir)
        if os.path.isdir(directory):
            for img_file in os.listdir(directory):
                new_img_file = img_file.replace('_', '')
                original_file = os.path.join(directory, img_file)
                new_file = os.path.join(directory, new_img_file)
                os.rename(original_file, new_file)

print('Done stripping out underscores.')
