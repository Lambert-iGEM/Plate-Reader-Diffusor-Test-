import os
from PIL import Image
import math


# open and split image 
def split():
    savedir = r"C:\Users\varun\Desktop\plateReader\DiffusorTest\savedIMG"
    filename = r"C:\Users\varun\Desktop\plateReader\DiffusorTest\testImages\test1.png"
    
    
    img = Image.open(filename).convert('L')
    width, height = img.size
    start_pos = start_x, start_y = (0, 0)
    splitDimensions = int(math.sqrt((width *height)/6))

    cropped_image_size = w, h = (splitDimensions,splitDimensions)

    frame_num = 1


    for col_i in range(0, width, w):
        for row_i in range(0, height, h):
            crop = img.crop((col_i, row_i, col_i + w, row_i + h))
            save_to= os.path.join(savedir, "testing_{:02}.png")
            crop.save(save_to.format(frame_num))
            frame_num += 1











