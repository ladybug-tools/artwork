import os

folder = os.path.dirname(os.path.realpath(__file__))
plugins = ['ladybug', 'honeybee', 'dragonfly']
subfolders = ['png', 'emoji']

for plugin in plugins:
    for subdir in subfolders:
        directory = os.path.join(folder, plugin, subdir)
        if os.path.isdir(directory):
            for img_file in os.listdir(directory):
                new_img_file = img_file.replace('_', '')
                original_file = os.path.join(directory, img_file)
                new_file = os.path.join(directory, new_img_file)
                os.rename(original_file, new_file)
