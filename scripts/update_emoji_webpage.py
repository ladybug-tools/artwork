"""This script updates the Ladybug Tools Emoji webpage with icons in emoji folders."""

import os
import re

# get the current directory
current_folder = os.path.dirname(os.path.realpath(__file__))
folder, scripts = os.path.split(current_folder)
emoji_page_folder = os.path.join(folder, 'emoji_webpage')

# parameters that get reused to build the ladybug-emoji.css
emoji_css_file = os.path.join(emoji_page_folder, 'ladybug-emoji.css')
artwork_href = 'https://github.com/ladybug-tools/artwork/raw/master'
css_text = '.em{height:1.5em;width:1.5em;background-position:center;'\
                'background-repeat:no-repeat;background-size:contain;display:'\
                'inline-block;vertical-align:middle}\n'

# parameters that get used to build the ladybug-emoji.html
emoji_html_file = os.path.join(emoji_page_folder, 'ladybug-emoji.html')
html_text_dict = {}


# fuction to pull off css and html text from images
def get_css_html(img_file, emoji_url):
    emoji_name = img_file.split('.')[0]
    emoji_css_text = '.em-{}{{background-image:url("{}")}}\n'.format(
        emoji_name, emoji_url)
    emoji_html_text = '        <li class="emoji" data-clipboard-text=":{}:">\n'\
        '          <i class="em em-{}"></i> :{}:\n'\
        '        </li>\n\n'.format(emoji_name, emoji_name, emoji_name)
    return emoji_name, emoji_css_text, emoji_html_text


# update all bug icons
html_text_dict['the bugs'] = ''
bug_directory = os.path.join(folder, 'icons_bugs', 'emoji')
for img_file in os.listdir(bug_directory):
    emoji_url = '{}/{}/{}/{}'.format(
        artwork_href, 'icons_bugs', 'emoji', img_file)
    emoji_name, emoji_css_text, emoji_html_text = get_css_html(
        img_file, emoji_url)
    css_text = css_text + emoji_css_text
    html_text_dict['the bugs'] = html_text_dict['the bugs'] + emoji_html_text

# update all of the component icons
icons_folder = 'icons_components'
plugins = ['ladybug', 'honeybee']

for plugin in plugins:
    html_text_dict[plugin] = ''
    directory = os.path.join(folder, icons_folder, plugin, 'emoji')
    if os.path.isdir(directory):
        for img_file in os.listdir(directory):
            emoji_url = '{}/{}/{}/{}/{}'.format(
                artwork_href, icons_folder, plugin, 'emoji', img_file)
            emoji_name, emoji_css_text, emoji_html_text = get_css_html(
                img_file, emoji_url)
            css_text = css_text + emoji_css_text
            html_text_dict[plugin] = html_text_dict[plugin] + emoji_html_text

# write all text into the css file
with open(emoji_css_file, 'w') as emoji_css:
    emoji_css.write(css_text)

# write all text into the html file
with open(emoji_html_file, 'r') as emoji_html:
    html_content = emoji_html.read()

for key in html_text_dict.keys():
    html_start_tag = '<!--START OF {} ICONS-->'.format(key.upper())
    html_end_tag = '<!--END OF {} ICONS-->'.format(key.upper())
    new_html = '{}\n{}        {}'.format(
        html_start_tag, html_text_dict[key], html_end_tag)
    re_str = '{}[\s\S]*{}'.format(html_start_tag, html_end_tag)
    pattern = re.compile(re_str)
    html_content = re.sub(pattern, new_html, html_content)

with open(emoji_html_file, 'w') as emoji_html:
    emoji_html.write(html_content)
