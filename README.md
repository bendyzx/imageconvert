# imageconvert by Ben Daluz 2020
imageconvert takes a source image, resizes it and maps the palette to best available from the 512 colours on the Spectrum Next. Of those, it picks the 256 most used colours and writes out a Spectrum Next compatible BMP or .nxi image with that palette. Non used palette entries are placed at the end of the range and set to 0,0,0

## Installation
imageconvert has been tested with Python 3.8. It may work with versions earlier than that but this is not guaranteed

## Usage:

* `py.exe -3.8 imageconvert.py sourcefile`
* `py.exe -3.8 imageconvert.py sourcefile -s 256,192`
* `py.exe -3.8 imageconvert.py sourcefile -c 256`
* `py.exe -3.8 imageconvert.py sourcefile -a`
* `py.exe -3.8 imageconvert.py sourcefile -g`
* `py.exe -3.8 imageconvert.py sourcefile -d`
* `py.exe -3.8 imageconvert.py sourcefile -o outputfile`

Any of the above arguments can be used in conjunction. e.g:

```py.exe -3.8 imageconvert.py test.jpg -s 256,192 -c 256 -a -g -d -o test.bmp```

default options are: ```-s 256,192 -c 256 -o ic-sourcefile```

**available options:**
* `-s x,y            image size`
* `-c                number of colours`
* `-a                maintain aspect ratio`
* `-g                greyscale`
* `-d                dither`
* `-o outputfile     specify output filename`

**n.b. the output filename extension determines the file format**

*if you dont specify the output filename with a different extension to the
  source, the output image will be in the same format as the source

*ImageConvert supports the .nxi filename extension
  This will output a Spectrum Next Layer 2 screen format with palette
  The file will be 49,664 bytes in size and contains the 256x192 pixels
  of layer 2 data prepended with 512 bytes of palette data (256 pairs
  of bytes in %RRRGGGBB, %P000000B format

