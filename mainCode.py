# this is an integrated python file with subtitles, borders, volume control and limited surgical cutting
from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip

# variables
srtSubs = 'ProjectMedia/I_LOVE_TO_SLEEP_twoSS.srt'
green_back_img = "ProjectMedia/green_back.png"
green_ender_img = "ProjectMedia/green_final.png"
video = "ProjectMedia/Clip-2-I-like-to-sleep.mp4"
video_start = "0:00:00"
video_end = "0:01:00"


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
	media = ImageClip(med).subclip(vid_st, vid_end)

	# determine how to resize the image to fit 9:16 aspect ratio
	# when y2=less, img=less: for clip2, when x1=more, left side cuts more, when x2=more, right side cuts less:
	if placement == "T":  # if it's placed at the top
		resized_img = media.crop(x1=0, x2=0, y1=0, y2=540)
		return resized_img
	elif placement == "B":  # if it's placed at the bottom
		resized_img = media.crop(x1=0, x2=0, y1=1380, y2=0)
		return resized_img
	elif placement == "V":  # if it's a video
		adjusted_vid = media.fx(afx.volumex, 3)
		resized_vid = adjusted_vid.crop(x1=120, x2=840, y1=0, y2=0).resize(1.5)
		return resized_vid
	else:  # else if it's the ender image
		return media


# assembles the clip and renders it
def clipAssembler(top_img, clip, bottom_img, subs, end_img):
	# creating the overlay with resized clips
	adding_clips = clips_array([[top_img], [clip], [bottom_img]])
	body = adding_clips.resize( (1080, 1920) )
	body_with_subs = CompositeVideoClip([body, subs])

	# cut six or less seconds of video
	with_cutting = body_with_subs.cutout(0, 0)

	# add the ender clip, title the video, and render
	final_clip = concatenate_videoclips([with_cutting, end_img])
	final_clip.write_videofile("renewed_code5.mp4")


# calling the functions
top_image = mediaManipulator(green_back_img, video_start, video_end, "T")
bottom_image = mediaManipulator(green_back_img, video_start, video_end, "B")
ender_image = mediaManipulator(green_ender_img, vid_st="0:00:00", vid_end="0:00:02")
video_clip = mediaManipulator(video, video_start, video_end, "V")
extracted_subs = subtitleExtractor(srtSubs, video_start, video_end)
clipAssembler(top_image, video_clip, bottom_image, extracted_subs, ender_image)

