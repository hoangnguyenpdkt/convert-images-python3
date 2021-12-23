#!/usr/bin/env python3
import PIL
import os, sys
from PIL import Image

dir="Images directory path"

file_list=[]

for filename in os.listdir(dir):
    f = os.path.join(dir, filename)
    # checking if it is a file
    if os.path.isfile(f):
        file_list.append(f)

for infile in file_list:
    f, e= os.path.splitext(infile)
    outfile = os.path.splitext(infile)[0] + ".jpeg"
    outfile =  outfile.replace("images","icons")
    if infile != outfile:
        try:
            with Image.open(infile) as im:
#JPG do not support transparency, we have to convert to RGB to discard transparency first
                im.convert("RGB").rotate(90).resize((128,128)).save(outfile,"JPEG")
        except OSError:
            print("cannot convert", infile)
