try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

from moviepy.editor import *
from functools import partial
mainWindow = tkinter.Tk()

mainWindow.title("Aleph Pro")
mainWindow.geometry('640x350-8-200')
mainWindow.configure(background="#282828")
mainWindow['padx'] = 10
icon = tkinter.PhotoImage(file="ProjectMedia/mbc-gold-vk favicon.png")
mainWindow.iconphoto(True, icon)


mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1)
mainWindow.columnconfigure(3, weight=1)
mainWindow.columnconfigure(4, weight=1)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=1)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=1)
mainWindow.rowconfigure(4, weight=1)

# FIRST HALF

border_firstHalf = tkinter.LabelFrame(mainWindow, bd=5, background="#383838")
border_firstHalf.grid(row=0, column=0, sticky="nw", pady=16)
border_firstHalf['padx'] = 11
border_firstHalf['pady'] = 7

label = tkinter.Label(border_firstHalf, text="Aleph Pro Video Editor",
                      background="#383838", fg='#0277bd')
label.grid(row=0, column=0, sticky="n")

# frame for the radio buttons

optionFrame = tkinter.LabelFrame(border_firstHalf, text="Color Options", background="#383838", fg='#0277bd')
optionFrame.grid(row=1, column=0, sticky='nw', pady=5)
rbValue = tkinter.IntVar()
rbValue.set(1)
# Radio buttons
radio1 = tkinter.Radiobutton(optionFrame, text="Blue Theme", value=1,
                             variable=rbValue, background="#383838",
                             fg='#0277bd')
radio2 = tkinter.Radiobutton(optionFrame, text="Green Theme", value=2,
                             variable=rbValue, background="#383838",
                             fg='#0277bd')
radio3 = tkinter.Radiobutton(optionFrame, text="Red Theme", value=3,
                             variable=rbValue, background="#383838",
                             fg='#0277bd')
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')
optionFrame['padx'] = 11
optionFrame['pady'] = 10

# Frame for the Name Entry
nameFrame = tkinter.LabelFrame(border_firstHalf, text="PowerClip Name",
                               height=40, width=125, background="#383838",
                               fg='#0277bd')
nameFrame.grid(row=2, column=0, sticky="nw", pady=5)
nameFrame['padx'] = 10
nameFrame['pady'] = 5
# Title of Powerclip
entry_4_name = tkinter.Entry(nameFrame, width=16, background="#444444")
entry_4_name.grid(row=0, column=0)

# Run button
runButton = tkinter.Button(border_firstHalf, text="Render", command=lambda: run_action(),
                           background="#444444", fg='#0277bd')
runButton.grid(row=3, column=0, sticky="n", pady=10)
# Spacing
spacing_label = tkinter.Label(border_firstHalf, text=' ', font=('Calibri', 17), background="#383838")
spacing_label.grid(row=4, column=0, sticky="n")

# SECOND HALF
# Entry boxes and Frames

border_second_half = tkinter.LabelFrame(mainWindow, bd=5, background="#383838")
border_second_half.grid(row=0, column=1, sticky='n', pady=16)
border_second_half['padx'] = 11
border_second_half['pady'] = 13


TopFrame = tkinter.LabelFrame(border_second_half, text="Sermon Video Filepath",
                              height=50, width=416, background="#383838",
                              fg='#0277bd')
TopFrame.grid(row=0, column=1, columnspan=1, sticky="n", pady=10)
TopFrame['padx'] = 10
TopFrame['pady'] = 5
# Sermon File Input line
entry1 = tkinter.Entry(TopFrame, width=65, background="#444444")
entry1.grid(row=0, column=0)

SecondFrame = tkinter.LabelFrame(border_second_half, text="Sermon Transcript Filepath",
                                 height=50, width=380, background="#383838", fg='#0277bd')
SecondFrame.grid(row=1, column=1, columnspan=1, sticky="w", pady=10)
SecondFrame['padx'] = 10
SecondFrame['pady'] = 5
# Transcript File Input line
entry2 = tkinter.Entry(SecondFrame, width=65, background="#444444")
entry2.grid(row=0, column=0)

ThirdFrame = tkinter.LabelFrame(border_second_half, text="Output Filepath",
                                height=50, width=380, background="#383838",
                                fg='#0277bd')
ThirdFrame.grid(row=2, column=1, columnspan=1, sticky="w", pady=10)
ThirdFrame['padx'] = 10
ThirdFrame['pady'] = 5
# Output Entry box
entry3 = tkinter.Entry(ThirdFrame, width=65, background="#444444")
entry3.grid(row=0, column=0)

FourthFrame = tkinter.LabelFrame(border_second_half, text="Start and Stop Marks (hh:mm:ss)",
                                 height=50, width=380, background="#383838", fg='#0277bd')
FourthFrame.grid(row=3, column=1, columnspan=1, sticky="w", pady=10)
FourthFrame['padx'] = 10
FourthFrame['pady'] = 5
entry4 = tkinter.Entry(FourthFrame, width=20, background="#444444")
entry5 = tkinter.Entry(FourthFrame, width=20, background="#444444")
entry4.grid(row=0, column=0, padx=10)
entry5.grid(row=0, column=1, padx=10)

# Editing Code


def create_vid():
    theme = rbValue.get()
    if theme == 1:  # if the green theme is selected
        back_img = "ProjectMedia/blue_back_2.6.1.png"
        ender_img = "ProjectMedia/blue_final_3.4.1.png"
    else:           # else the blue theme is selected
        back_img = "ProjectMedia/green_back.png"
        ender_img = "ProjectMedia/green_final.png"

    video_start = "0:32:20"
    video_end = "0:32:23"
    title = entry_4_name.get()
    clip1 = ImageClip("{}".format(back_img)).subclip(video_start, video_end)
    new_clips = VideoFileClip("C:\\Users\\Gabriel\\OneDrive\\MBC Folder\\21-Broadcast\\21f-Raw Sermon Video\\Saved Sermons\\Pay Attention To Last Words.mp4").subclip(video_start, video_end)
    clip3 = ImageClip("{}".format(back_img)).subclip(video_start, video_end)
    ender_clip = ImageClip("{}".format(ender_img)).subclip("0:00:00", "0:00:02")
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
    final_clip.write_videofile("C:\\Users\\Gabriel\\OneDrive\\MBC Folder\\29-Gen-Z\\29d-Finished Clips\\{}.mp4".format(title), fps=final_clip.fps)


run_action = partial(create_vid)

mainWindow.mainloop()
