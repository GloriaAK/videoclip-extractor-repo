try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

from moviepy.editor import *
from functools import partial
from moviepy.video.tools.subtitles import SubtitlesClip
import tkinter as tk
from PIL import ImageTk, Image
from resizeimage import resizeimage  # install as python-resize-image
from tkinter import filedialog as fd

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
# Border for the First Half Section

border_firstHalf = tkinter.LabelFrame(mainWindow, bd=5, background="#383838")
border_firstHalf.grid(row=0, column=0, sticky="nw", pady=16)
border_firstHalf['padx'] = 11
border_firstHalf['pady'] = 7
# Title Label
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

# Frame for the Powerclip Name Entry
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
# Frame for sermon filepath
TopFrame = tkinter.LabelFrame(border_second_half, text="Sermon Video Filepath",
                              height=50, width=416, background="#383838",
                              fg='#0277bd')
TopFrame.grid(row=0, column=1, columnspan=1, sticky="n", pady=10)
TopFrame['padx'] = 10
TopFrame['pady'] = 5
# Sermon File Entry box
entry1 = tkinter.Entry(TopFrame, width=65, background="#444444")
entry1.grid(row=0, column=0)

# Frame for Sermon Transcript Filepath
SecondFrame = tkinter.LabelFrame(border_second_half, text="Sermon Transcript Filepath",
                                 height=50, width=380, background="#383838", fg='#0277bd')
SecondFrame.grid(row=1, column=1, columnspan=1, sticky="w", pady=10)
SecondFrame['padx'] = 10
SecondFrame['pady'] = 5
# Transcript File Entry box
entry2 = tkinter.Entry(SecondFrame, width=65, background="#444444")
entry2.grid(row=0, column=0)

# Frame for Output Filepath
ThirdFrame = tkinter.LabelFrame(border_second_half, text="Output Filepath",
                                height=50, width=380, background="#383838",
                                fg='#0277bd')
ThirdFrame.grid(row=2, column=1, columnspan=1, sticky="w", pady=10)
ThirdFrame['padx'] = 10
ThirdFrame['pady'] = 5
# Output Entry box
entry3 = tkinter.Entry(ThirdFrame, width=65, background="#444444")
entry3.grid(row=0, column=0)

# Frame and entries for start and stop timecodes
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
def select_file():
    filetypes = (('audio files', '*.mp3'), ('All files', '*.*'))
    music_filename = fd.askopenfilename(title='Select a Music File', initialdir='/', filetypes=filetypes)
    return music_filename


def subtitleExtractor(sub_file, vid_st, vid_end):
    generator = lambda txt: TextClip(txt, font='Calibri', fontsize=75, color='white')
    subs = SubtitlesClip(sub_file, generator)
    subtitle_edits1 = subs.subclip(vid_st, vid_end)
    subtitle_edits2 = subtitle_edits1.set_position('top').margin(top=20, opacity=0)

    return subtitle_edits2


def mediaManipulator(med, vid_st, vid_end, placement):
    # determine how to resize the image to fit 9:16 aspect ratio
    # when y2=less, img=less: for clip2, when x1=more, left side cuts more, when x2=more, right side cuts less:
    if placement == "T":  # if it's placed at the top
        media = ImageClip(med).subclip(vid_st, vid_end)
        resized_img = media.crop(x1=0, x2=0, y1=0, y2=540)
        return resized_img
    elif placement == "B":  # if it's placed at the bottom
        media = ImageClip(med).subclip(vid_st, vid_end)
        resized_img = media.crop(x1=0, x2=0, y1=1380, y2=0)
        return resized_img
    elif placement == "V":  # if it's a video
        media = VideoFileClip(med).subclip(vid_st, vid_end)
        adjusted_vid = media
        if round(media.fps, 3) <= 20.000:  # if it's a video filmed at 20 frames per second, use these crop numbers
            resized_vid = adjusted_vid.crop(x1=160, x2=1120, y1=0, y2=0).resize(1.125)
        elif round(media.fps, 3) >= 23.000:  # if it's a video filmed at 24 frames per second, use these crop numbers
            resized_vid = adjusted_vid.crop(x1=120, x2=840, y1=0, y2=0).resize(1.5)
        else:
            resized_vid = adjusted_vid.crop(x1=120, x2=840, y1=0, y2=0).resize(1.5)  # else, you're pretty much screwed, just do whatever

        return resized_vid
    else:  # else if it's the ender image
        media = ImageClip(med).subclip(vid_st, vid_end)
        return media


def clipAssembler(top_img, clip, bottom_img, subs, end_img):
    # creating the overlay with resized clips
    adding_clips = clips_array([[top_img], [clip], [bottom_img]])
    body = adding_clips.resize((1080, 1920))
    body_with_subs = CompositeVideoClip([body, subs])

    # cut six or fewer seconds of video
    # with_cutting = body_with_subs.cutout(0, 0)

    # add the ender clip
    final_video_clip = concatenate_videoclips([body_with_subs, end_img])
    return final_video_clip


def audioAdditionAndFinalization(final_video, music_path, title):
    narration = final_video.audio
    narration.fx(afx.volumex, 3)
    music = AudioFileClip(music_path).fx(afx.volumex, 0.25)
    music_over_words = CompositeAudioClip([narration, music])  # .set_fps(44100) use this if you've removed it from .write_videofile
    final_audio_and_video = final_video.set_audio(music_over_words)
    final_audio_and_video.write_videofile("{}".format(title), fps=final_video.fps)



def finalize_video():
    theme = rbValue.get()
    if theme == 1:  # if the blue theme is selected
        back_img = "ProjectMedia/blue_back_2.6.1.png"
        ender_img = "ProjectMedia/blue_final_3.4.1.png"
    elif theme == 2:  # if the green theme is selected
        back_img = "ProjectMedia/green_back.png"
        ender_img = "ProjectMedia/green_final.png"
    else:           # else the red theme is selected
        back_img = "ProjectMedia/red_border_img_1.1.1.png"
        ender_img = "ProjectMedia/red_ender_img_1.1.1.png"
    video = entry1.get()
    srt_subs = entry2.get()
    end_dir_path = entry3.get()
    video_START = entry4.get()
    video_end = entry5.get()
    clip_name = entry_4_name.get()
    name_place = end_dir_path + "\\" + clip_name + ".mp4"

    top_image = mediaManipulator(back_img, video_START, video_end, "T")
    bottom_image = mediaManipulator(back_img, video_START, video_end, "B")
    ender_image = mediaManipulator(ender_img, vid_st="0:00:00", vid_end="0:00:02", placement="E")
    video_clip = mediaManipulator(video, video_START, video_end, "V")
    extracted_subs = subtitleExtractor(srt_subs, video_START, video_end)
    final_video_clip = clipAssembler(top_image, video_clip, bottom_image, extracted_subs, ender_image)
    music_filename = select_file()
    audioAdditionAndFinalization(final_video_clip, music_filename, name_place)

if __name__ == '__main__':
    run_action = partial(finalize_video)


mainWindow.mainloop()
