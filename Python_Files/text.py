from moviepy.editor import *
myvideo1 = VideoFileClip("clip1.mp4")
myvideo2 = VideoFileClip("clip2.mp4")
myvideo3 = VideoFileClip("clip3.mp4")
final_clip = concatenate_videoclips([myvideo1,myvideo2,myvideo3])
final_clip.write_videofile("my_concatenation.mp4")