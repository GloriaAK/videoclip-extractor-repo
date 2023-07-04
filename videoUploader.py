"""
This script uses the requests library to send a POST request to the URL http://your-website.com/upload with the video
file as a multipart/form-data file.

Note: This is just a basic example to get you started. You'll need to modify the code to handle any additional
parameters, error handling, and response parsing that your website requires.
"""

# import requests
#
# url = "http://your-website.com/upload"
# video = open("path/to/video.mp4", "rb")
#
# files = {'video': ('video.mp4', video, 'video/mp4')}
#
# response = requests.post(url, files=files)
#
# if response.status_code == 200:
#     print("Upload successful")
# else:
#     print("Upload failed")
#
# video.close()

"""Below is a file explorer opener. A simplified version of this is in mainCodeGui.py"""

# import tkinter as tk
# from tkinter import *
# from tkinter import filedialog as fd
#
# # create the root window
# root = tk.Tk()
# root.title('Tkinter Open File Dialog')
# root.resizable(True, True)
# root.geometry('600x350')
#
# def select_file():
#     filetypes = (('audio files', '*.mp3'), ('All files', '*.*'))
#     filename = fd.askopenfilename(title='Open a file', initialdir='/', filetypes=filetypes)
#     label_path = Label(root, text=filename, font=('italic 14'))
#     label_path.pack(pady=20)
#
#
# open_btn = tk.Button(root, text='Open a File', command=select_file)
# open_btn.pack()
#
# root.mainloop()

"""Below is a stripped down version of mainCodeGui.py used for debugging purposes"""

from moviepy.editor import *
import tkinter as tk
from functools import partial

# root window
root = tk.Tk()
root.geometry("790x890")
root.title('MBC Video Editor')
root.resizable(None, None)
icon = tk.PhotoImage(file="ProjectMedia/mbc-gold-vk favicon.png")
root.iconphoto(True, icon)
root.configure(background="#282828")



def create_vid(theme):
    if theme == 1:  # if the green theme is selected
        back_img = "ProjectMedia/green_back.png"
        ender_img = "ProjectMedia/green_final.png"
    else:           # else the blue theme is selected
        back_img = "ProjectMedia/blue_back_2.6.1.png"
        ender_img = "ProjectMedia/blue_final_3.4.1.png"
    video_start = "0:32:20"
    video_end = "0:32:23"
    title = ent1.get()
    clip1 = ImageClip("{}".format(back_img)).subclip(video_start, video_end)
    new_clips = VideoFileClip("C:\\Users\\Gabriel\\OneDrive\\MBC Folder\\21-Broadcast\\21f-Raw Sermon Video\\Saved Sermons\\Pay Attention To Last Words.mp4").subclip(video_start, video_end)
    clip3 = ImageClip("{}".format(ender_img)).subclip(video_start, video_end)
    ender_clip = ImageClip("ProjectMedia/green_final.png").subclip("0:00:00", "0:00:02")
    # when y2=less, img=less: for clip2, when x1=more, left side cuts more, when x2=more, right side cuts less:

    if round(new_clips.fps, 3) == 20.000:
        resized_clip1 = clip1.crop(x1=0, x2=0, y1=0, y2=540)
        resized_clip2 = new_clips.crop(x1=160, x2=1120, y1=0, y2=0).resize(1.125)
        resized_clip3 = clip3.crop(x1=0, x2=0, y1=1380, y2=0)
    elif round(new_clips.fps, 3) == 23.976:
        resized_clip1 = clip1.crop(x1=0, x2=0, y1=0, y2=540)
        resized_clip2 = new_clips.crop(x1=120, x2=840, y1=0, y2=0).resize(1.5)
        resized_clip3 = clip3.crop(x1=0, x2=0, y1=1380, y2=0)
    else:
        resized_clip1 = clip1.crop(x1=0, x2=0, y1=0, y2=540)
        resized_clip2 = new_clips.crop(x1=120, x2=840, y1=0, y2=0).resize(1.5)
        resized_clip3 = clip3.crop(x1=0, x2=0, y1=1380, y2=0)

    adding_clips = clips_array([[resized_clip1], [resized_clip2], [resized_clip3]])
    body = adding_clips.resize((1080, 1920))

    final_clip = concatenate_videoclips([body, ender_clip])
    final_clip.write_videofile("C:\\Users\\Gabriel\\OneDrive\\MBC Folder\\29-Gen-Z\\29b-Finished Clips\\{}.mp4".format(title), fps=final_clip.fps)


grn_action = partial(create_vid, 1)
bl_action = partial(create_vid, 2)
ent1 = tk.Entry(root, font=('Calibri', 14), background="#383838", width=70, fg='white')
ent1.grid(column=2, row=2, padx=10, pady=2)

exe_bnt1 = tk.Button(root, font=('Calibri', 14), text='Create A green Power Clip', command=lambda: grn_action(), width=45,
                     background="#383838", fg='white')
exe_bnt2 = tk.Button(root, font=('Calibri', 14), text='Create A blue Power Clip', command=lambda: bl_action(), width=45,
                     background="#383838", fg='white')

exe_bnt1.grid(column=2, row=7, padx=10, pady=10)
exe_bnt2.grid(column=2, row=8, padx=10, pady=10)

root.mainloop()
