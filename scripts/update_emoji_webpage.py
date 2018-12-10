"""This script updates the Ladybug Tools Emoji webpage with icons in emoji folders."""

import os

# get the current directory
current_folder = os.path.dirname(os.path.realpath(__file__))
folder, scripts = os.path.split(current_folder)

# text that gets reused to build the ladybug-emoji.css
artwork_href = 'https://github.com/ladybug-tools/artwork/raw/master/'
css_start_text = '.em,.em-svg{height:1.5em;width:1.5em;background-position:center;'\
                'background-repeat:no-repeat;background-size:contain;display:'\
                'inline-block;vertical-align:middle}\n'


# update all of the component icons
icons_folder = 'icons_components'
plugins = ['ladybug', 'honeybee']
subfolder = 'emoji'
