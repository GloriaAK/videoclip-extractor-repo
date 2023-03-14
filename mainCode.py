# this is an integrated python file with subtitles, borders, volume control and limited surgical cutting
from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip

# variables for uploaded SRT file and video start and end times to be clipped
srtSubs = 'ProjectMedia/I_LOVE_TO_SLEEP_twoSS.srt'
video_start = "0:00:00"
video_end = "0:01:00"

# takes a srt file, a start time, an end time, and extracts subtitles between the time specified
def subtitleExtractor(sub_file, vid_st, vid_en):
	generator = lambda txt: TextClip(txt, font='Calibri', fontsize=75, color='white')
	subs = SubtitlesClip(sub_file, generator)
	subtitles = SubtitlesClip(subs, generator)
	subtitle_edits1 = subtitles.subclip(vid_st, vid_en)
	subtitle_edits2 = subtitle_edits1.set_position('top').margin(top=20, opacity=0)

	return subtitle_edits2

extracted_subs = subtitleExtractor(srtSubs, video_start, video_end)

# import and clip videos, as well as volume control
clip1 = ImageClip("ProjectMedia/green_back.png").subclip(video_start, video_end)
clip2 = VideoFileClip("ProjectMedia/Clip-2-I-like-to-sleep.mp4").subclip(video_start, video_end).fx(afx.volumex, 3)
clip3 = ImageClip("ProjectMedia/green_back.png").subclip(video_start, video_end)
ender_clip = ImageClip("ProjectMedia/green_final.png").subclip("0:00:00", "0:00:02")

# resize clips for 9:16 ratio format
# when y2=less, img=less: for clip2, when x1=more, left side cuts more, when x2=more, right side cuts less:
resized_clip1 = clip1.crop(x1=0, x2=0, y1=0, y2=540)
resized_clip2 = clip2.crop(x1=120, x2=840, y1=0, y2=0).resize(1.5)
resized_clip3 = clip3.crop(x1=0, x2=0, y1=1380, y2=0)

# creating the overlay with resized clips
adding_clips = clips_array([[resized_clip1], [resized_clip2], [resized_clip3]])
body = adding_clips.resize( (1080, 1920) )
body_with_subs = CompositeVideoClip([body, extracted_subs])

# cut six or less seconds of video
with_cutting = body_with_subs.cutout(5, 6)

# add the ender clip, title the video, and render
final_clip = concatenate_videoclips([with_cutting, ender_clip])
final_clip.write_videofile("renewed_code5.mp4")

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
how to printout the runtime envirnment within an exe in windows 10
'''