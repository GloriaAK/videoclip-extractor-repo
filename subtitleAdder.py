from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.tools.subtitles import SubtitlesClip

# Load the video file
video = VideoFileClip("ProjectMedia/Clip-2-I-like-to-sleep.mp4")

# Load the subtitles from the .vtt file
subtitles = SubtitlesClip("ProjectMedia/I_like_to_sleep.vtt", video.fps)

# Combine the video and subtitles
final_video = video.set_audio(video.audio).set_subtitles(subtitles)

# Write the final video to file
final_video.write_videofile(r"C:\Users\glori\OneDrive\MBC Folder\29-Gen-Z\PythonExtractorClips\new_clip_subtitles.mp4", codec='mpeg4')

print("Success!")
