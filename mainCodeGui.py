from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
import tkinter as tk
from PIL import ImageTk, Image
from resizeimage import resizeimage  # install as python-resize-image
from functools import partial

# root window
root = tk.Tk()
root.geometry("790x880")
root.title('MBC Video Editor')
root.resizable(None, None)
icon = tk.PhotoImage(file="ProjectMedia/mbc-gold-vk favicon.png")
root.iconphoto(True, icon)
root.configure(background="#282828")

# takes a srt file, a start time, an end time, and extracts subtitles between the time specified
def subtitleExtractor(sub_file, vid_st, vid_end):
    generator = lambda txt: TextClip(txt, font='Calibri', fontsize=75, color='white')
    subs = SubtitlesClip(sub_file, generator)
    subtitles = SubtitlesClip(subs, generator)
    subtitle_edits1 = subtitles.subclip(vid_st, vid_end)
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
        adjusted_vid = media.fx(afx.volumex, 3)
        resized_vid = adjusted_vid.crop(x1=120, x2=840, y1=0, y2=0).resize(1.5)
        return resized_vid
    else:  # else if it's the ender image
        media = ImageClip(med).subclip(vid_st, vid_end)
        return media


def clipAssembler(top_img, clip, bottom_img, subs, end_img, name_place):
    # creating the overlay with resized clips
    adding_clips = clips_array([[top_img], [clip], [bottom_img]])
    body = adding_clips.resize( (1080, 1920) )
    body_with_subs = CompositeVideoClip([body, subs])

    # cut six or less seconds of video
    with_cutting = body_with_subs.cutout(0, 0)

    # add the ender clip, title the video, and render
    final_clip = concatenate_videoclips([with_cutting, end_img])
    final_clip.write_videofile("{}".format(name_place))


def finalize_video(theme):
    if theme == 1:  # if the green theme is selected
        back_img = "ProjectMedia/green_back.png"
        ender_img = "ProjectMedia/green_final.png"
    else:  # else if the blue theme is selected
        back_img = "ProjectMedia/blue_back_2.6.1.png"
        ender_img = "ProjectMedia/blue_final_3.4.1.png"

    video = ent1.get()
    end_dir_path = ent2.get()
    video_START = ent3.get()
    video_end = ent4.get()
    clip_name = ent5.get()
    name_place = end_dir_path + "\\" + clip_name + ".mp4"
    srt_subs = ent6.get()

    top_image = mediaManipulator(back_img, video_START, video_end, "T")
    bottom_image = mediaManipulator(back_img, video_START, video_end, "B")
    ender_image = mediaManipulator(ender_img, vid_st="0:00:00", vid_end="0:00:02", placement="E")
    video_clip = mediaManipulator(video, video_START, video_end, "V")
    extracted_subs = subtitleExtractor(srt_subs, video_START, video_end)
    clipAssembler(top_image, video_clip, bottom_image, extracted_subs, ender_image, name_place)


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


# just two buttons... nothing to see
grn_action = partial(finalize_video, 1)
bl_action = partial(finalize_video, 2)
green_btn = tk.Button(root, font=('Calibri', 14), text="Run with green theme", command=grn_action, width=25, background="#383838", fg='white')
blue_btn = tk.Button(root, font=('Calibri', 14), text="Run with blue theme", command=bl_action, width=25, background="#383838", fg='white')
green_btn.grid(column=2, row=13, padx=5, pady=10)
blue_btn.grid(column=2, row=14, padx=5, pady=10)

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
text4.grid(column=2, row=7, padx=5, pady=2)
text5.grid(column=2, row=9, padx=5, pady=2)
text6.grid(column=2, row=11, padx=5, pady=2)

# Input spaces
ent1 = tk.Entry(root, font=('Calibri', 14), background="#383838", width=70, fg='white')
ent6 = tk.Entry(root, font=('Calibri', 14), background="#383838", width=70, fg='white')
ent2 = tk.Entry(root, font=('Calibri', 14), background="#383838", width=70, fg='white')
ent3 = tk.Entry(root, font=('Calibri', 14), background="#383838", width=20, fg='white')
ent4 = tk.Entry(root, font=('Calibri', 14), background="#383838", width=20, fg='white')
ent5 = tk.Entry(root, font=('Calibri', 14), background="#383838", width=20, fg='white')

ent1.grid(column=2, row=2, padx=5, pady=2)
ent6.grid(column=2, row=4, padx=5, pady=2)
ent2.grid(column=2, row=6, padx=5, pady=2)
ent3.grid(column=2, row=8, padx=5, pady=2)
ent4.grid(column=2, row=10, padx=5, pady=2)
ent5.grid(column=2, row=12, padx=5, pady=2)

root.mainloop()
