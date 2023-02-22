from moviepy.editor import *
video_start = "0:00:00"
video_end = "0:00:35"
clip1 = ImageClip("ProjectMedia/green_back.png").subclip(video_start, video_end)
clip2 = VideoFileClip("ProjectMedia/Clip-2-I-like-to-sleep.mp4").subclip(video_start, video_end).fx(afx.volumex, 3)
clip3 = ImageClip("ProjectMedia/green_back.png").subclip(video_start, video_end)
ender_clip = ImageClip("ProjectMedia/green_final.png").subclip("0:00:00", "0:00:02")
# when y2=less, img=less: for clip2, when x1=more, left side cuts more, when x2=more, right side cuts less:
resized_clip1 = clip1.crop(x1=0, x2=0, y1=0, y2=540)
resized_clip2 = clip2.crop(x1=120, x2=840, y1=0, y2=0).resize(1.5)
resized_clip3 = clip3.crop(x1=0, x2=0, y1=1380, y2=0)

adding_clips = clips_array([[resized_clip1], [resized_clip2], [resized_clip3]])
body = adding_clips.resize( (1080, 1920) )

# cut_start = '0:00:08:00'
# cut_end = '0:00:24:00'
final_body = body.cutout("0:00:08", "0:00:24")  # ‘01:03:05.35’

final_clip = concatenate_videoclips([final_body, ender_clip])
final_clip.write_videofile("vid_clip_Man7.mp4")
