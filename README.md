imageconvert by Ben Daluz 2020
------------------------------
imageconvert usage:

- py.exe -3.8 imageconvert.py <filename>
- py.exe -3.8 imageconvert.py <filename> -s 256,192
- py.exe -3.8 imageconvert.py <filename> -c 256
- py.exe -3.8 imageconvert.py <filename> -a
- py.exe -3.8 imageconvert.py <filename> -g
- py.exe -3.8 imageconvert.py <filename> -d
- py.exe -3.8 imageconvert.py <filename> -o <outputfile>

Any of the above arguments can be used in conjunction. e.g:

- py.exe -3.8 imageconvert.py test.jpg -s 256,192 -c 256 -a -g -d -o test.bmp

default options are: -s 256,192 -c 256 -o ic-<filename>
     
n.b. the output filename extension determines the file format
- if you dont specify the output filename with a different extension to the
  source, the output image will be in the same format as the source
