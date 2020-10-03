from tkinter import filedialog
from tkinter import *
from moviepy.editor import *
root =Tk()
def trim():
            try:   
               #global file
               myvideo1 = VideoFileClip("DO NOT OPEN - 1 Minute Film.mp4")
               myvideoedited = myvideo1.subclip(6,11)
               myvideoedited.write_videofile('trimclip.mp4',codec='libx264') 
               myvideoedited.preview()
               root.quit()
            except IOError:
                           pass
            

button7= Button(root,text="...",command=trim).place(x=800,y=110)
root.mainloop()