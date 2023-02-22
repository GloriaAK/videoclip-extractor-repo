# this is an integrated python file with subtitles, borders, volume control and limited surgical cutting
from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip

# subtitle generator
generator = lambda txt: TextClip(txt, font='Calibri', fontsize=90, color='white')
subs = SubtitlesClip('ProjectMedia/I_LOVE_TO_SLEEP_twoSS.srt', generator)
subtitles = SubtitlesClip(subs, generator)

# import and crop videos, volume control, and determine vid length
video_start = "0:00:00"
video_end = "0:01:10"
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
body_with_subs = CompositeVideoClip([body, subtitles.set_pos(('center', 'top'))])

with_cutting = body_with_subs.cutout(8, 14)
final_clip = concatenate_videoclips([with_cutting, ender_clip])
final_clip.write_videofile("renewed_code1.mp4")

'''
# this is a subtitle adder
from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip

generator = lambda txt: TextClip(txt, font='Arial', fontsize=34, color='white')
subs = SubtitlesClip('ProjectMedia/I_LOVE_TO_SLEEP_twoSS.srt', generator)
subtitles = SubtitlesClip(subs, generator)

video = VideoFileClip("ProjectMedia/Clip-2-I-like-to-sleep.mp4")
result = CompositeVideoClip([video, subtitles.set_pos(('center', 'bottom'))])

result.write_videofile("testingStuff_Vid2.mp4")

'''