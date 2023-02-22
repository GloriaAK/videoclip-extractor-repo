# import pip
# pip.main(['install','moviepy'])
from moviepy.editor import *

clip2_video = VideoFileClip("Clip-1-smash-and-grab.mp4")

# internal surgical clipping
# cut_start = "00:00:08.00"
# cut_end = "00:00:12.00"

# clip1 = clip2_video.subclip(0, 8)
# clip2 = clip2_video.subclip(24, 74)
# vid_body = concatenate_videoclips([clip1, clip2])
cut1 = 5
cut2 = 10
cut3 = 10
cut4 = 15

changing = clip2_video.cutout(5, 15)

# newhope = changing.cutout(5, 10)
# newhope2 = newhope.cutout(5, 10)

changing.set_duration(75).write_videofile("original_code123.mp4")

# array = clip.audio.to_soundarray(fps=44100)
# clip = VideoFileClip(r"PATH_TO_MOVEIEPY_MEDIA_DIRECTORY/video_with_failing_audio.mp4")
# array = clip.audio.to_soundarray(fps=30)
"""cut1 = int(input("cut one timecode"))
cut2 = int(input("cut two timecode"))
cut3 = int(input("cut three timecode"))
cut4 = int(input("cut four timecode"))"""