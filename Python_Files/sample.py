from moviepy.editor import *
def trim():
           try:   
            myvideo1 = VideoFileClip("DO NOT OPEN - 1 Minute Film.mp4")
            myvideoedited = myvideo1.fx( vfx.speedx, 0.5) # double the speed
            myvideoedited.write_videofile('clip3.mp4',codec='libx264')
            myvideoedited.preview()
           except IOError:
                  pass
trim()