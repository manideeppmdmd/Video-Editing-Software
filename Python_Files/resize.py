from moviepy.editor import *
myvideo1 = VideoFileClip("DO NOT OPEN - 1 Minute Film.mp4")
myvideoedited = myvideo1.fx( vfx.resize, width=460) # resize (keep aspect ratio)
myvideoedited.write_videofile('clip2.mp4',codec='libx264')