# Introduction

Your company is in the process of updating its website, and they've hired a design contractor to create some new icon graphics for the site. But the contractor has delivered the final designs in the wrong format -- rotated 90° and too large. Oof! You're not able to get in contact with the designers and your own deadline is approaching fast. You'll need to use Python to get these images ready for launch.
## What you’ll do

Use the Python Imaging Library to do the following to a batch of images:

	Open an image

	Rotate an image

	Resize an image

	Save an image in a specific format in a separate directory 
## Install Pillow

We should change the format and size of these pictures, and rotate them by 90° clockwise. To do this, we'll use Python Imaging Library (PIL). Install pillow library using the following command:
```
	pip3 install pillow
```
## Script file
Edit script file
```
	nano convert_images.py
```
Add the folling lines:

```python
#!/usr/bin/env python3
import PIL
import os, sys
from PIL import Image
dir="/home/nguyenpham/images"
#new_dir="/home/nguyenpham/icons"
file_list=[]

for filename in os.listdir(dir):
    f = os.path.join(dir, filename)
    # checking if it is a file
    if os.path.isfile(f):
        file_list.append(f)
#print(file_list)
for infile in file_list:
    f, e= os.path.splitext(infile)
    #print(f)
    #outfile=f.replace("images","icons")+"jpeg"
    #print(outfile)
    outfile = os.path.splitext(infile)[0] + ".jpeg"
    outfile =  outfile.replace("images","icons")
    #print(outfile)
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                #out=im.rotate(90).save(outfile)
                #im.resize((128,128)).save(outfile)
                #im.save(outfile)
                im.convert("RGB").rotate(90).resize((128,128)).save(outfile,"JPEG")
        except OSError:
            print("cannot convert", infile)
```
## Grant executable permission to the script file
```
	chmod +x convert_images.py
```
## Now, run the file.
```
	./convert_images.py
```

Copyright: Google IT Automation with Python Professional Certificate
