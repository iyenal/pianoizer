from moviepy.editor import *
from moviepy import *
import moviepy

clip = VideoFileClip("Interstellar.mp4")

clip.save_frame("preview.png", t = 7 )

# Crop the video to the zone of the actual piano scrolling sheet
clip = moviepy.video.fx.all.crop(clip, x1=0, y1=5, x2=640, y2=170)

# Your configuration here
start = 6 #when the piano playing starts (seconds)
interval = 3 #at what interval the notes in one given frame are finished to be played, can be found by trial (seconds)
length = 10 #how much intermediary sheets (frame files) you would like to be considered for generating the sheet

def pianoize(start, interval, length):
    time = start
    list_i = []

    # saving a frame at 2 second
    for x in range(length):
        name = "frame"+str(x)+".png"
        list_i.append(name)
        clip.save_frame(name, t = time )
        time+=interval

    list_i.reverse()

    import sys
    from PIL import Image, ImageOps

    images = [Image.open(x) for x in list_i]
    widths, heights = zip(*(i.size for i in images))

    total_width = max(widths)
    max_height = sum(heights)

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for im in images:
      new_im.paste(im, (0,x_offset))
      x_offset += im.size[1]

    new_im = ImageOps.flip(new_im)

    # optional: draw lines to help reading

    new_im.save("result_"+str(interval)+".jpg")
    
#for i in range(30):
    #pianoize(6,1+(i/10),10)

pianoize(6,2.25,200)

%pylab inline
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img = mpimg.imread('result.jpg')
imgplot = plt.imshow(img)
plt.show()

print("Done.")