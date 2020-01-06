## minimalQuote

![alt text](https://i.imgur.com/nr2Ssit.png "Example")

## Dependencies:

* ImageMagick: [Create, edit, compose, or convert bitmap images](https://imagemagick.org/script/download.php)

* Utilizes [wand](http://docs.wand-py.org/en/0.5.8/) and [nider](https://github.com/pythad/nider)
  * Install pip packages in `requirements.txt`
    * `pip3 install --upgrade -r requirements.txt`

## Usage:

`minimalQuote.py [-h] [--batch] [--color COLOR] width height`

positional arguments:
  * width: Width of background to be generated
  * height: Height of background to be generated

optional arguments:
  * -h, --help: show this help message and exit
  * --batch: Generate backgrounds from predefined list of quotes
    * Example in this repository is `silicon_valley_quotes.txt`
    * If utilizing this option, format your quote list in the same was as shown:
      * `\n;\n` as the delimiter between quote/author pairs
      * `|` (pipe) as the delimiter between quote and author
  * --color COLOR: Hex color code; will generate ALL background with this color code