"""import pysrt
subs = pysrt.open("ProjectMedia/I_LOVE_TO_SLEEP_twoSS.srt")

# for i in subs:
#     # print(sub.text)
#     ace123 = i.text
#     aa = ace123[0:5]
#     print(aa)
#
# ace123 = subs.text
# for i in subs.text:
#     if i == len(ace123[0:5])
listings = subs.text.split()
print(listings)
"""

from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip
video_start = "0:00:00"
video_end = "0:00:10"

generator = lambda txt: TextClip(txt, font='Arial', fontsize=70, color='white')
subs = SubtitlesClip('ProjectMedia/I_LOVE_TO_SLEEP_twoSS.srt', generator)
subtitles = SubtitlesClip(subs, generator)

subtile_edits1 = subtitles.subclip(video_start, video_end)
subtile_edits2 = subtile_edits1.set_position('top').margin(top=20, opacity=0)

video = VideoFileClip("ProjectMedia/Clip-2-I-like-to-sleep.mp4").subclip(video_start, video_end)
result = CompositeVideoClip([video, subtile_edits2])

result.write_videofile("subtitleMargins15.mp4")