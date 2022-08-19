from tkinter import *
from tkvideo import tkvideo

root =Tk()

root.title('Rishabh player')

video_label = Label(root)
video_label.pack()
player = tkvideo("Digital_clock.mp4",video_label,loop=1,size=(700,400))
player.play()
root.mainloop()