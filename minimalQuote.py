import argparse
import os
import random
import uuid
import getpass

from nider.core import Font
from nider.core import Outline

from nider.models import Content
from nider.models import Header
from nider.models import Paragraph
from nider.models import Image as nider_image
from nider.models import Linkback

from wand.image import Image
from argparse import RawTextHelpFormatter

result_path = '/results/'
# Replace this path with your desired font path
font_path = "/Users/" + getpass.getuser() + "/Library/Fonts/Aileron-Heavy.otf"
text_outline = Outline(1, '#000000')

# Parser definition and setup
parser = argparse.ArgumentParser(description='Script to generate simple, minimalistic, quote backgrounds\nDefault action is to create from single quote', formatter_class=RawTextHelpFormatter)
parser.add_argument('width', type=str, help='Width of background to be generated')
parser.add_argument('height', type=str, help='Height of background to be generated')
parser.add_argument('--batch', action='store_true', help='Generate backgrounds from predefined list of quotes')
parser.add_argument('--color', type=str, help='Hex color code; will generate ALL background with this color code')
args = parser.parse_args()

# Function to generate background
def generate_background(color, mq_width, mq_height, quote, author, name):
  path = os.getcwd()
  res_path = path + result_path + str(name) + '.png'
  header = Header(text=quote,
                  font=Font(font_path, 120),
                  text_width=40,
                  align='left',
                  color='#000000',
                  outline=text_outline
                  )
  linkback = Linkback(text=author,
                      font=Font(font_path, 70),
                      color='#000000',
                      outline=text_outline,
                      align='left',
                      bottom_padding=200
                      )

  content = Content(header=header, linkback=linkback)

  img = nider_image(content,
                    fullpath=res_path,
                    width=int(mq_width),
                    height=int(mq_height)
                    )

  img.draw_on_bg(color)

# Function to parse predefined list of quotes
def parse_quote_file(quote_src):
  quote_arr = list()
  parse_arr = list()
  all_quotes = None
  with open(quote_src, 'r') as f:
    all_quotes = f.read()
  parse_arr = all_quotes.split("\n;\n\n")
  for q in parse_arr:
    indiv_arr = q.split("|\n")
    indiv_arr[1]= indiv_arr[1].rstrip('\n')
    quote_arr.append(indiv_arr)
  return quote_arr

def main():
  # Predefined color list
  color_list = ["#ff8a80", "#8c9eff", "#82b1ff", "#b9f6ca", "#ccff90", "#f4ff81", "#ffff8d", "#ffe57f", "#ffd180", "#ff9e80"]
  # Get args
  mq_width = args.width
  mq_height = args.height
  batch = args.batch
  color = args.color
  # Single quote
  if batch is True:
    print('Enter path to quote file:')
    quote_src = input()
    quote_arr = parse_quote_file(quote_src)
    for q in quote_arr:
      generate_background(random.choice(color_list), mq_width, mq_height, q[0], q[1], str(uuid.uuid4().hex))
    return
  else:
    print('Enter quote:')
    quote = input()
    print('Enter quotee: ')
    author = input()
    generate_background(random.choice(color_list), mq_width, mq_height, quote, author, str(uuid.uuid4().hex))
    return

main()