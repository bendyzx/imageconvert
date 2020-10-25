#!/usr/bin/env python3

# ImageConvert
# Ben Daluz
# https://github.com/bendyzx/imageconvert
# released under the unlicense, see http://unlicense.org 
# (practically public domain) 

from lxml import html
from datetime import date, timedelta, time
from PIL import Image
from io import BytesIO
from shutil import copyfileobj
import requests
import sys
import ChromeController
import time
import math
import glob
import timeit
import datetime
import io

assert sys.version_info >= (3, 6)

if __name__ == "__main__":
    import sys, os

sourcefile = None
targetfile = None
size = [256, 192]
colours = 256
maintainaspect = True
greyscale = False
dither = False

palette512 = [0,0,0,0,0,36,0,0,73,0,0,109,0,0,146,0,0,182,0,0,219,0,0,255,0,36,0,0,36,36,0,36,73,0,36,109,0,36,146,0,36,182,0,36,219,0,36,255,0,73,0,0,73,36,0,73,73,0,73,109,0,73,146,0,73,182,0,73,219,0,73,255,0,109,0,0,109,36,0,109,73,0,109,109,0,109,146,0,109,182,0,109,219,0,109,255,0,146,0,0,146,36,0,146,73,0,146,109,0,146,146,0,146,182,0,146,219,0,146,255,0,182,0,0,182,36,0,182,73,0,182,109,0,182,146,0,182,182,0,182,219,0,182,255,0,219,0,0,219,36,0,219,73,0,219,109,0,219,146,0,219,182,0,219,219,0,219,255,0,255,0,0,255,36,0,255,73,0,255,109,0,255,146,0,255,182,0,255,219,0,255,255,36,0,0,36,0,36,36,0,73,36,0,109,36,0,146,36,0,182,36,0,219,36,0,255,36,36,0,36,36,36,36,36,73,36,36,109,36,36,146,36,36,182,36,36,219,36,36,255,36,73,0,36,73,36,36,73,73,36,73,109,36,73,146,36,73,182,36,73,219,36,73,255,36,109,0,36,109,36,36,109,73,36,109,109,36,109,146,36,109,182,36,109,219,36,109,255,36,146,0,36,146,36,36,146,73,36,146,109,36,146,146,36,146,182,36,146,219,36,146,255,36,182,0,36,182,36,36,182,73,36,182,109,36,182,146,36,182,182,36,182,219,36,182,255,36,219,0,36,219,36,36,219,73,36,219,109,36,219,146,36,219,182,36,219,219,36,219,255,36,255,0,36,255,36,36,255,73,36,255,109,36,255,146,36,255,182,36,255,219,36,255,255,73,0,0,73,0,36,73,0,73,73,0,109,73,0,146,73,0,182,73,0,219,73,0,255,73,36,0,73,36,36,73,36,73,73,36,109,73,36,146,73,36,182,73,36,219,73,36,255,73,73,0,73,73,36,73,73,73,73,73,109,73,73,146,73,73,182,73,73,219,73,73,255,73,109,0,73,109,36,73,109,73,73,109,109,73,109,146,73,109,182,73,109,219,73,109,255,73,146,0,73,146,36,73,146,73,73,146,109,73,146,146,73,146,182,73,146,219,73,146,255,73,182,0,73,182,36,73,182,73,73,182,109,73,182,146,73,182,182,73,182,219,73,182,255,73,219,0,73,219,36,73,219,73,73,219,109,73,219,146,73,219,182,73,219,219,73,219,255,73,255,0,73,255,36,73,255,73,73,255,109,73,255,146,73,255,182,73,255,219,73,255,255,109,0,0,109,0,36,109,0,73,109,0,109,109,0,146,109,0,182,109,0,219,109,0,255,109,36,0,109,36,36,109,36,73,109,36,109,109,36,146,109,36,182,109,36,219,109,36,255,109,73,0,109,73,36,109,73,73,109,73,109,109,73,146,109,73,182,109,73,219,109,73,255,109,109,0,109,109,36,109,109,73,109,109,109,109,109,146,109,109,182,109,109,219,109,109,255,109,146,0,109,146,36,109,146,73,109,146,109,109,146,146,109,146,182,109,146,219,109,146,255,109,182,0,109,182,36,109,182,73,109,182,109,109,182,146,109,182,182,109,182,219,109,182,255,109,219,0,109,219,36,109,219,73,109,219,109,109,219,146,109,219,182,109,219,219,109,219,255,109,255,0,109,255,36,109,255,73,109,255,109,109,255,146,109,255,182,109,255,219,109,255,255,146,0,0,146,0,36,146,0,73,146,0,109,146,0,146,146,0,182,146,0,219,146,0,255,146,36,0,146,36,36,146,36,73,146,36,109,146,36,146,146,36,182,146,36,219,146,36,255,146,73,0,146,73,36,146,73,73,146,73,109,146,73,146,146,73,182,146,73,219,146,73,255,146,109,0,146,109,36,146,109,73,146,109,109,146,109,146,146,109,182,146,109,219,146,109,255,146,146,0,146,146,36,146,146,73,146,146,109,146,146,146,146,146,182,146,146,219,146,146,255,146,182,0,146,182,36,146,182,73,146,182,109,146,182,146,146,182,182,146,182,219,146,182,255,146,219,0,146,219,36,146,219,73,146,219,109,146,219,146,146,219,182,146,219,219,146,219,255,146,255,0,146,255,36,146,255,73,146,255,109,146,255,146,146,255,182,146,255,219,146,255,255,182,0,0,182,0,36,182,0,73,182,0,109,182,0,146,182,0,182,182,0,219,182,0,255,182,36,0,182,36,36,182,36,73,182,36,109,182,36,146,182,36,182,182,36,219,182,36,255,182,73,0,182,73,36,182,73,73,182,73,109,182,73,146,182,73,182,182,73,219,182,73,255,182,109,0,182,109,36,182,109,73,182,109,109,182,109,146,182,109,182,182,109,219,182,109,255,182,146,0,182,146,36,182,146,73,182,146,109,182,146,146,182,146,182,182,146,219,182,146,255,182,182,0,182,182,36,182,182,73,182,182,109,182,182,146,182,182,182,182,182,219,182,182,255,182,219,0,182,219,36,182,219,73,182,219,109,182,219,146,182,219,182,182,219,219,182,219,255,182,255,0,182,255,36,182,255,73,182,255,109,182,255,146,182,255,182,182,255,219,182,255,255,219,0,0,219,0,36,219,0,73,219,0,109,219,0,146,219,0,182,219,0,219,219,0,255,219,36,0,219,36,36,219,36,73,219,36,109,219,36,146,219,36,182,219,36,219,219,36,255,219,73,0,219,73,36,219,73,73,219,73,109,219,73,146,219,73,182,219,73,219,219,73,255,219,109,0,219,109,36,219,109,73,219,109,109,219,109,146,219,109,182,219,109,219,219,109,255,219,146,0,219,146,36,219,146,73,219,146,109,219,146,146,219,146,182,219,146,219,219,146,255,219,182,0,219,182,36,219,182,73,219,182,109,219,182,146,219,182,182,219,182,219,219,182,255,219,219,0,219,219,36,219,219,73,219,219,109,219,219,146,219,219,182,219,219,219,219,219,255,219,255,0,219,255,36,219,255,73,219,255,109,219,255,146,219,255,182,219,255,219,219,255,255,255,0,0,255,0,36,255,0,73,255,0,109,255,0,146,255,0,182,255,0,219,255,0,255,255,36,0,255,36,36,255,36,73,255,36,109,255,36,146,255,36,182,255,36,219,255,36,255,255,73,0,255,73,36,255,73,73,255,73,109,255,73,146,255,73,182,255,73,219,255,73,255,255,109,0,255,109,36,255,109,73,255,109,109,255,109,146,255,109,182,255,109,219,255,109,255,255,146,0,255,146,36,255,146,73,255,146,109,255,146,146,255,146,182,255,146,219,255,146,255,255,182,0,255,182,36,255,182,73,255,182,109,255,182,146,255,182,182,255,182,219,255,182,255,255,219,0,255,219,36,255,219,73,255,219,109,255,219,146,255,219,182,255,219,219,255,219,255,255,255,0,255,255,36,255,255,73,255,255,109,255,255,146,255,255,182,255,255,219,255,255,255]
palettedictionary = [[[None for y in range(256)] for z in range(256)] for v in range(256)]

def resizeImage(image):
    x = size[0]
    y = size[1]
    if maintainaspect:
        ratio = min(size[0] / image.width, size[1] / image.height)
        x = (int)(ratio * image.width)
        y = (int)(ratio * image.height)
    image = image.resize((x, y))
    xos = 0
    yos = 0
    if x < size[0]:
        xos = (int)((size[0] - x) / 2)
    if y < size[1]:
        yos = (int)((size[1] - y) / 2)
    if xos > 0 or yos > 0:
        newImage = Image.new('RGB', (size[0], size[1]), (0, 0, 0))
        newImage.paste(image, (xos, yos, xos + x, yos + y))
        return newImage        
    return image.convert("RGB")

def Get3bitColor(col):
    if col < 19:
        c = 0
    else:
        if col < 54:       #36
            c = 1
        else:
            if col < 91:      #73
                c = 2
            else:
                if col < 127:     #109
                    c = 3
                else:
                    if col < 164:     #146
                        c = 4
                    else:
                        if col < 200:     #182
                            c = 5
                        else:
                            if col < 237:     #219
                                c = 6
                            else:
                                c = 7
    return c

def getBestPalette(image):
    global palettedictionary

    width, height = image.size
    pixels = image.load()
    newpalettelength = int(colours * 3)
    newpalette = [0 for x in range(newpalettelength)]
    ps = int(len(palette512) /3)
    pu = [[0,-1, 0,0] for x in range(ps)]
    pc = 0
    for i in range(width):
        for j in range(height):
            red, green, blue = pixels[i, j]
            if palettedictionary[red][green][blue] is None:
                r = Get3bitColor(red)
                g = Get3bitColor(green)
                b = Get3bitColor(blue)
                palettedictionary[red][green][blue] = (64 * r) + (8 * g) + b
            pin = palettedictionary[red][green][blue]
            pi = [idx for idx,element in enumerate(pu) if element[1] == pin]
            if len(pi) == 0:
                pu[pc] = [1, pin]
                pc += 1            
            else:
                pu[pi[0]][0] += 1                
    pos = 0
    pu.sort(reverse=True)
    pu = pu[0 : 256]
    for u in pu:
        pp = pos * 3
        if u[0] > 0:
            uu = u[1] * 3
            if pos < colours:
                newpalette[pp] = palette512[uu] 
                newpalette[pp + 1] = palette512[uu + 1] 
                newpalette[pp + 2] = palette512[uu + 2]            
        pos = pos + 1
    return newpalette

def savegreyscale(image):
    width, height = image.size
    pixels = image.load()
    gsimage = Image.new('RGB', (width, height), (0, 0, 0))
    gspixels = gsimage.load()
    for i in range(width):
        for j in range(height):
            red, green, blue = pixels[i, j]
            gray = (red * 0.299) + (green * 0.587) + (blue * 0.114)
            gspixels[i, j] = (int(gray), int(gray), int(gray))
    saveimage(gsimage)

def processimage():
    image = Image.open(sourcefile)
    scaledImage = resizeImage(image)
    if greyscale:
        savegreyscale(scaledImage)
    else:
        saveimage(scaledImage)

def saveNxi(image, targetfile):
    buf = io.BytesIO()
    image.save(buf, format='BMP')
    filedata = buf.getvalue()
    newfiledata = b''
    for p in range(54, 1078, 4):
        B = Get3bitColor(filedata[p])
        G = Get3bitColor(filedata[p + 1])
        R = Get3bitColor(filedata[p + 2])
        p1 = (R << 5)
        p1 |= (G << 2)
        p1 |= (B >> 1)
        p2 = B & 1
        newfiledata += p1.to_bytes(1, "big") + p2.to_bytes(1, "big")
    for b in range(50229, 1077, -256):
        for c in range(255, -1, -1):
            newfiledata += filedata[b - c].to_bytes(1, "big")
    with open(targetfile, 'wb') as tgtfile:
        tgtfile.write(newfiledata)

def saveimage(image):
    d = math.ceil(math.sqrt(colours))
    palimage = Image.new('P', (d, d))
    pal = getBestPalette(image)
    palimage.putpalette(pal)
    newimage = quantizetopalette(image, palimage)
    if targetfile.endswith('.nxi'):
        saveNxi(newimage, targetfile)
    else:
        try:
            newimage.save(targetfile)
        except:
            newimage.convert('RGB').save(targetfile)

def quantizetopalette(image, palette):
    """Convert an RGB or L mode image to use a given P image's palette."""
    image.load()
    # use palette from reference image made below
    palette.load()
    d = 0
    if dither:
        d = 1
    im = image.im.convert("P", d, palette.im)
    return image._new(im)

def info():
    print(f'------------------------------')
    print(f'imageconvert usage:\n')
    print(f'imageconvert <filename>')
    print(f'imageconvert <filename> -s 256,192')
    print(f'imageconvert <filename> -c 256')
    print(f'imageconvert <filename> -a')
    print(f'imageconvert <filename> -g')
    print(f'imageconvert <filename> -d')
    print(f'imageconvert <filename> -o <outputfile>\n')
    print(f'Any of the above arguments can be used in conjunction. e.g:\n')
    print(f'imageconvert test.jpg -s 256,192 -c 256 -a -g -d -o test.bmp\n')
    print(f'default options are: -s 256,192 -c 256 -o ic-<filename>\n')
    print(f'available options:\n')
    print(f' - s x,y            image size')
    print(f' - c                number of colours')
    print(f' - a                maintain aspect ratio')
    print(f' - g                greyscale')
    print(f' - d                dither')
    print(f' - o outputfile     specify output filename\n')
    print(f'n.b. the output filename extension determines the file format\n')
    print(f' - if you dont specify the output filename with a different extension to the')
    print(f'   source, the output image will be in the same format as the source\n')
    print(f' - ImageConvert supports the .nxi filename extension')
    print(f'   This will output a Spectrum Next Layer 2 screen format with palette')
    print(f'   The file will be 49,664 bytes in size and contains the 256x192 pixels')
    print(f'   of layer 2 data prepended with 512 bytes of palette data (256 pairs')
    print(f'   of bytes in %RRRGGGBB, %P000000B format')

print(f'------------------------------')
print(f'imageconvert by Ben Daluz 2020')
if len(sys.argv) == 1:
    info()
    quit()
sourcefile = sys.argv[1]
if not os.path.exists(sourcefile):
    print(f'\n')
    print(f'sourcefile {sourcefile} does not exist')
    quit()
targetname = sourcefile.split('\\')[-1]
targetfile = f'ic-{targetname}'
lastarg = None
getnextval = False
for x in sys.argv[2:]:
    if getnextval:
        if lastarg == "size":
            try:
                size = [ int(a) for a in x.split(',') ]
            except:
                print(f'\nBad following argument value for {lastarg}')  
                info()
                quit()
        if lastarg == "cols":
            try:
                colours = int(x)
            except:
                print(f'\nBad following argument value for {lastarg}')  
                info()
                quit()
        if lastarg == "target":
            targetfile = x
        getnextval = False
    if x == "-s":
        getnextval = True
        lastarg = "size"
    if x == "-c":
        getnextval = True
        lastarg = "cols"
    if x == "-a":
        maintainaspect = False
        lastarg = None
    if x == "-g":
        greyscale = True
        lastarg = None
    if x == "-d":
        dither = True
        lastarg = None
    if x == "-o":
        lastarg = "target"
        getnextval = True

if getnextval:
    print(f'\nMissing argument value for {lastarg}')  
    info()
    quit()

processimage()
print(f'output: {targetfile}')