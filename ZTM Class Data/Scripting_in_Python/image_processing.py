import os
import sys
from PIL import Image

# grabs the first and second arguements
image_folder = sys.argv[0]
output_folder = sys.argv[1]

# check is new/exist, if not creates one
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
