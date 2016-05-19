# vesper-gen
A simple library viewer for the vesper icons font icon library... This is a Flask web app written in Python. Really there is hardly any code. It simply parses the CSS file into a web page showing all icons in the file.

The font icons are from https://github.com/kkvesper/vesper-icons and may be used very permissively without attribution, but I'd still like to thank the creators:

Vesper Icons by KK Vesper - http://kkvesper.jp

### Install
Currently I don't have anything fancy, but you should be able to clone this locally and run *vesper-gen.py* with Python (written on 3.4.4). If you don't have Flask installed, you'll want to install it with *pip install flask*. Once running, you can access the rendered icon library at http://127.0.0.1:5000/

![vesper-page](/static/images/vesper-page.PNG?raw=true "vesper-page")

### License
- Code written by me in this archive is dedicated to the public domain and able to be used in any way without attribution. Code, docs and fonts from the Vesper Icon font are not covered by this dedication but are instead under a permissive license compatible with Font Awesome. See the following points for more information...
- The Vesper Icons font is licensed under the SIL OFL 1.1:
  - http://scripts.sil.org/OFL
- Vesper Icons CSS and other source code files are licensed under the MIT License:
  - http://opensource.org/licenses/mit-license.html
- The Vesper Icons documentation is licensed under the CC BY 3.0 License:
  - http://creativecommons.org/licenses/by/3.0/
