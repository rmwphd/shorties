# python script for generating What Ya Working On? trifolds
# Supports up to six projects.
# 
# Usage: call from command line
#    python WYWOT.py "project name 1" "project name 2" ... "project name 6"
# then print the resulting webpage. 
# Next, fold the sheet in half, then fold each half in half. Lastly, 
# tuck the blank quarter behind the top quarter and tape! 
# The fill order is top-to-bottom right-side-up, then 
# top-to-bottom upside-down.
 
import os
import sys
import webbrowser

def WYWOT(*args):
    proj = []
    for i in range(6):
        try:
            proj.append(args[i])
        except: 
            proj.append(' ')

    html = '<!DOCTYPE html>\
    <html>\
    <body>\
    \
    <svg height="900" width="800" xmlns:xlink="http://www.w3.org/1999/xlink">\
    <text x="50" y="90" fill="blue" font-family="Verdana" font-size="78">%s</text>\
    <text x="0" y="-60" fill="red" font-family="Verdana" font-size="78" \
    transform="rotate(180 380,30)">%s</text>\
    <text x="50" y="360" fill="green" font-family="Verdana" font-size="78">%s</text>\
    <text x="0" y="-330" fill="blue" font-family="Verdana" font-size="78" \
    transform="rotate(180 380,30)">%s</text>\
    <text x="50" y="630" fill="red" font-family="Verdana" font-size="78">%s</text>\
    <text x="0" y="-600" fill="green" font-family="Verdana" font-size="78" \
    transform="rotate(180 380,30)">%s</text>\
    Sorry, your browser does not support inline SVG.\
    </svg>\
    </body>\
    </html>' % (proj[0], proj[3], proj[1], proj[4], proj[2], proj[5])

    path = os.path.abspath('wywot.html')
    url = 'file://' + path

    with open(path, 'w') as f:
        f.write(html)
        webbrowser.open(url)

callwith = []
for i in range(1,len(sys.argv)):
    callwith.append(sys.argv[i])

WYWOT(*callwith)
