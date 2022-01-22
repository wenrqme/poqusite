"""
This scrip resizes all images in a directory and converts them to jpeg

input directory: large/
output directory: resized/

"""

import os
import glob
from PIL import Image
import sys

IN_FOLDER = 'large/'
OUT_FOLDER = 'portfolio/'

args = sys.argv
if len(args) > 3:
    print ("too many arguments")
    quit()

# if there are no arguments use default folders
if len(args) == 3:
    print('folders found')
    IN_FOLDER = args[1] + '/'
    OUT_FOLDER = args[2] + '/'



#resize all images to this width
width = 1200

for file in glob.glob(IN_FOLDER + '*'):
    file_base = os.path.basename(file)[:-4]
    output_file = OUT_FOLDER + '/' + file_base + '.jpg'
    print(file_base)
    print(output_file)

    #only resize if images are not already the directory
    if not os.path.exists(output_file):
        print("resizing!")
        img = Image.open(file)
        icc_profile = img.info.get('icc_profile')
        w_percent = width/float(img.size[0])
        height = int(float(img.size[1])*float(w_percent))
        new_img = img.resize((width, height), Image.ANTIALIAS)
        new_img = new_img.convert('RGB')
        new_img.save(output_file, icc_profile=icc_profile, quality=95)
    else:
        print('already here, not resizing!')

print('yeeee we done!!')
