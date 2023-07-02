from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
import tkinter as tk
from PIL import ImageTk, Image
from resizeimage import resizeimage  # install as python-resize-image
from functools import partial
from tkinter import filedialog as fd

# root window
root = tk.Tk()
root.geometry("790x890")
root.title('MBC Video Editor')
root.resizable(None, None)
icon = tk.PhotoImage(file="ProjectMedia/mbc-gold-vk favicon.png")
root.iconphoto(True, icon)
root.configure(background="#282828")

# function below opens file explorer and selects a file
def select_file():
    filetypes = (('audio files', '*.mp3'), ('All files', '*.*'))
    music_filename = fd.askopenfilename(title='Select a Music File', initialdir='/', filetypes=filetypes)
    return music_filename


# takes a srt file, a start time, an end time, and extracts subtitles between the time specified
def subtitleExtractor(sub_file, vid_st, vid_end):
    generator = lambda txt: TextClip(txt, font='Calibri', fontsize=75, color='white')
    subs = SubtitlesClip(sub_file, generator)
    # subtitles = SubtitlesClip(subs, generator)
    subtitle_edits1 = subs.subclip(vid_st, vid_end)
    subtitle_edits2 = subtitle_edits1.set_position('top').margin(top=20, opacity=0)

    return subtitle_edits2


# extracts a clip/image using the specified start and end times, adjusts the aspect ratio, and does volume control
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


# assembles the clip and renders it
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
    music_over_words = CompositeAudioClip([narration, music])  # .set_fps(44100)
    final_audio_and_video = final_video.set_audio(music_over_words)
    final_audio_and_video.write_videofile("{}".format(title), fps=final_video.fps)


def finalize_video(theme):
    if theme == 1:  # if the green theme is selected
        back_img = "ProjectMedia/green_back.png"
        ender_img = "ProjectMedia/green_final.png"
    else:           # else the blue theme is selected
        back_img = "ProjectMedia/blue_back_2.6.1.png"
        ender_img = "ProjectMedia/blue_final_3.4.1.png"
    video = ent1.get()
    srt_subs = ent_2.get()
    end_dir_path = ent_3.get()
    video_START = ent_4.get()
    video_end = ent_5.get()
    clip_name = ent_6.get()
    name_place = end_dir_path + "\\" + clip_name + ".mp4"

    top_image = mediaManipulator(back_img, video_START, video_end, "T")
    bottom_image = mediaManipulator(back_img, video_START, video_end, "B")
    ender_image = mediaManipulator(ender_img, vid_st="0:00:00", vid_end="0:00:02", placement="E")
    video_clip = mediaManipulator(video, video_START, video_end, "V")
    extracted_subs = subtitleExtractor(srt_subs, video_START, video_end)
    final_video_clip = clipAssembler(top_image, video_clip, bottom_image, extracted_subs, ender_image)
    music_filename = select_file()
    audioAdditionAndFinalization(final_video_clip, music_filename, name_place)


root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)
# logo image
path = "ProjectMedia/Top GUI Logo 1.1_6.1.1.png"
img = Image.open(path)
resized = resizeimage.resize_thumbnail(img, [450, 358])
# initialize
new_pic = ImageTk.PhotoImage(resized)
panel = tk.Label(image=new_pic, borderwidth=0)
panel.grid(column=2, row=0, padx=1, pady=1)


# two run buttons and file explorer function
grn_action = partial(finalize_video, 1)
bl_action = partial(finalize_video, 2)
# open_btn = tk.Button(root, font=('Calibri', 14), text='Select a Music File', command=select_file, width=45, background="#383838", fg='white')
green_btn = tk.Button(root, font=('Calibri', 14), text="Run with green theme", command=lambda: grn_action(), width=25, background="#383838", fg='white')
blue_btn = tk.Button(root, font=('Calibri', 14), text="Run with blue theme", command=lambda: bl_action(), width=25, background="#383838", fg='white')

# open_btn.grid(column=2, row=7, padx=5, pady=10)
green_btn.grid(column=2, row=14, padx=5, pady=10)
blue_btn.grid(column=2, row=15, padx=5, pady=10)


# overhead text
text1 = tk.Label(root, font=('Calibri', 16), background='#282828', text="Enter the file path for the sermon video", fg='white')
text2 = tk.Label(root, font=('Calibri', 16), background='#282828', text="""Enter the file path for the SRT file""", fg='white')
text3 = tk.Label(root, font=('Calibri', 16), background='#282828', text="Enter the file path for the location you want the clip saved", fg='white')
text4 = tk.Label(root, font=('Calibri', 16), background='#282828', text="Enter starting timestamp for the clip\n you want extracted. Format as hh:mm:ss", fg='white')
text5 = tk.Label(root, font=('Calibri', 16), background='#282828', text="Enter ending timestamp for the clip\nyou want extracted. Format as hh:mm:ss", fg='white')
text6 = tk.Label(root, font=('Calibri', 16), background='#282828', text="""Enter a name for the new clip, then press "Run" """, fg='white')

text1.grid(column=2, row=1, padx=1, pady=1)
text2.grid(column=2, row=3, padx=5, pady=2)
text3.grid(column=2, row=5, padx=5, pady=2)
text4.grid(column=2, row=8, padx=5, pady=2)
text5.grid(column=2, row=10, padx=5, pady=2)
text6.grid(column=2, row=12, padx=5, pady=2)

# Input spaces
ent1 = tk.Entry(root, font=('Calibri', 14), background="#383838", width=70, fg='white')
ent_2 = tk.Entry(root, font=('Calibri', 14), background="#383838", width=70, fg='white')
ent_3 = tk.Entry(root, font=('Calibri', 14), background="#383838", width=70, fg='white')
ent_4 = tk.Entry(root, font=('Calibri', 14), background="#383838", width=20, fg='white')
ent_5 = tk.Entry(root, font=('Calibri', 14), background="#383838", width=20, fg='white')
ent_6 = tk.Entry(root, font=('Calibri', 14), background="#383838", width=20, fg='white')

ent1.grid(column=2, row=2, padx=5, pady=2)
ent_2.grid(column=2, row=4, padx=5, pady=2)
ent_3.grid(column=2, row=6, padx=5, pady=2)
ent_4.grid(column=2, row=9, padx=5, pady=2)
ent_5.grid(column=2, row=11, padx=5, pady=2)
ent_6.grid(column=2, row=13, padx=5, pady=2)

root.mainloop()
