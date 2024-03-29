# this is an integrated python file with subtitles, borders, volume control and limited surgical cutting
from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip

"""If after you download ImageMagick, you get a error stating "[WinError 2] The system cannot find the file specified.
.This error can be due to the fact that ImageMagick is not installed on your computer, or (for Windows users) that you
 didn't specify the path to the ImageMagick binary in file conf.py, or that the path you specified is incorrect",
  then uncomment the following two lines"""
# from moviepy.config import change_settings
# change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"})
# variables

"""The commented out lines below are used to test different types of media in the editor."""
# srtSubs = 'ProjectMedia/I_LOVE_TO_SLEEP_twoSS.srt'
# green_back_img = "ProjectMedia/green_back.png"
# green_ender_img = "ProjectMedia/green_final.png"
# video = "ProjectMedia/Clip-2-I-like-to-sleep.mp4"
# video_start = "0:00:01"
# video_end = "0:00:04"
srtSubs = 'C:\\Users\\Gabriel\\OneDrive\\MBC Folder\\29-Gen-Z\\29a-Raw Clips\\20230416 clips\\auto_generated_srt_captions.srt'
green_back_img = "ProjectMedia/green_back.png"
green_ender_img = "ProjectMedia/green_final.png"
video = "C:\\Users\\Gabriel\\OneDrive\\MBC Folder\\21-Broadcast\\21f-Raw Sermon Video\\Saved Sermons\\Faithful Men In Evil Days.mp4"
music_audio = "C:\\Users\\Gabriel\\OneDrive\\MBC Folder\\29-Gen-Z\\Music\\TenderMusic\\Tender30_5.mp3"
video_start = "0:27:32"
video_end = "0:28:00"


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
		adjusted_vid = media
		if round(media.fps, 3) == 20.000:  # if it's a video filmed at 20 frames per second, use these crop numbers
			resized_vid = adjusted_vid.crop(x1=160, x2=1120, y1=0, y2=0).resize(1.125)
		elif round(media.fps, 3) == 23.976:  # if it's a video filmed at 24 frames per second, use these crop numbers
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

	# cut six or less seconds of video
	with_cutting = body_with_subs.cutout(0, 0)

	# add the ender clip
	final_video_clip = concatenate_videoclips([with_cutting, end_img])
	return final_video_clip


def audioAdditionAndFinalization(final_video, music_path):
	narration = final_video.audio
	narration.fx(afx.volumex, 3)
	music = AudioFileClip(music_path).fx(afx.volumex, 0.25)
	music_over_words = CompositeAudioClip([narration, music])  # .set_fps(44100)
	final_audio_and_video = final_video.set_audio(music_over_words)
	final_audio_and_video.write_videofile("NewCodeResult03.mp4", fps=final_video.fps)


# calling the functions
top_image = mediaManipulator(green_back_img, video_start, video_end, "T")
bottom_image = mediaManipulator(green_back_img, video_start, video_end, "B")
ender_image = mediaManipulator(green_ender_img, vid_st="0:00:00", vid_end="0:00:02", placement="E")
video_clip = mediaManipulator(video, video_start, video_end, "V")
extracted_subs = subtitleExtractor(srtSubs, video_start, video_end)
final_video_clip = clipAssembler(top_image, video_clip, bottom_image, extracted_subs, ender_image)
audioAdditionAndFinalization(final_video_clip, music_audio)

# @decorator.decorator
# def apply_to_audio(f, clip, *a, **k):
#     """ This decorator will apply the function f to the audio of
#         the clip created with f """
#
#     newclip = f(clip, *a, **k)
#     if getattr(newclip, 'audio', None):
#         newclip.audio = f(newclip.audio, *a, **k) #change second newclip to clip
#     return newclip
