from moviepy.editor import *
myvideo1 = VideoFileClip("DO NOT OPEN - 1 Minute Film.mp4")
myvideoedited = myvideo1.subclip(6,11)
myvideoedited.write_videofile('clip1.mp4',codec='libx264')
myvideoedited.show()