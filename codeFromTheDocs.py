# from moviepy.editor import *
# import moviepy.audio.fx.all as afx
# video = VideoFileClip("ProjectMedia/Clip-1.mp4").subclip(24, 69)
# music = AudioFileClip('ProjectMedia/Ardie-45-7.wav')   # .fx(afx.volumex, 0.5)
#
# video1 = CompositeVideoClip([video])
# audio = CompositeAudioClip([video, music])
#
# music2 = CompositeVideoClip([video1, audio])
#
# music2.write_videofile("musicArdie1.mp4")
"""
Result: https://www.youtube.com/watch?v=Qu7HJrsEYFg

This is how we can imagine knights dancing at the 15th century, based on a very
serious historical study here: https://www.youtube.com/watch?v=zvCvOC2VwDc

Here is what we do:

0. Get the video of a dancing knight, and a (Creative Commons) audio music file.
1. Load the audio file and automatically find the tempo.
2. Load the video and automatically find a segment that loops well
3. Extract this segment, slow it down so that it matches the audio tempo, and make
   it loop forever.
4. Symmetrize this segment so that we will get two knights instead of one
5. Add a title screen and some credits, write to a file.

This example has been originally edited in an IPython Notebook, which makes it
easy to preview and fine-tune each part of the editing.
"""


import os
import sys

from moviepy.editor import *
from moviepy.audio.tools.cuts import find_audio_period
from moviepy.video.tools.cuts import find_video_period


audio = (
    AudioFileClip("ProjectMedia/Ardie-45-7.wav")
    .subclip(0.1, 5)
    .audio_fadein(1)
    .audio_fadeout(1)
)

# LOAD, EDIT, ANALYZE THE VIDEO

clip = (
    VideoFileClip("ProjectMedia/Clip-2-I-like-to-sleep.mp4", audio=True)
    .subclip(0.1, 5)
    .crop(x1=500, x2=1350)
)

dancing_knights = clip.set_audio(audio, clip)



# MAKE THE TITLE SCREEN

txt_title = (
    TextClip(
        "15th century dancing\n(hypothetical)",
        fontsize=50,
        font="Century-Schoolbook-Roman",
        color="white",
    )

    .margin(top=15, opacity=0)
    .set_position(("center", "top"))
)

title = (
    CompositeVideoClip([dancing_knights.to_ImageClip(), txt_title])
    .fadein(0.5)
    .set_duration(3.5)
)


# MAKE THE CREDITS SCREEN

txt_credits = """
CREDITS

Video excerpt: Le combat en armure au XVe siècle
By J. Donzé, D. Jaquet, T. Schmuziger,
Université de Genève, Musée National de Moyen Age

Music: "Frontier", by DOCTOR VOX
Under licence Creative Commons
https://www.youtube.com/user/DOCTORVOXofficial

Video editing © Zulko 2014
 Licence Creative Commons (CC BY 4.0)
Edited with MoviePy: http://zulko.github.io/moviepy/
"""

credits = (
    TextClip(
        txt_credits,
        color="white",
        font="Century-Schoolbook-Roman",
        fontsize=35,
        kerning=-2,
        interline=-1,
        bg_color="black",
        size=title.size,
    )
    .set_duration(2.5)
    .fadein(0.5)
    .fadeout(0.5)
)

# ASSEMBLE EVERYTHING, WRITE TO FILE

final = concatenate_videoclips([title, dancing_knights, credits])

final.write_videofile(
    "dancing_knights8.mp4", fps=clip.fps, audio_bitrate="1000k", bitrate="4000k"
)