# # import pip
# # pip.main(['install','moviepy'])
# from moviepy.editor import *
#
# clip2_video = VideoFileClip("ProjectMedia/Clip-1-smash-and-grab.mp4")
#
# # internal surgical clipping
# # cut_start = "00:00:08.00"
# # cut_end = "00:00:12.00"
#
# # clip1 = clip2_video.subclip(0, 8)
# # clip2 = clip2_video.subclip(24, 74)
# # vid_body = concatenate_videoclips([clip1, clip2])
#
# changing = clip2_video.cutout(5, 11)
# # newhope = changing.cutout(5, 10)
# # newhope2 = newhope.cutout(5, 10)
#
# changing.write_videofile("original_code125.mp4")
#
#
# # array = clip.audio.to_soundarray(fps=44100)
# # clip = VideoFileClip(r"PATH_TO_MOVEIEPY_MEDIA_DIRECTORY/video_with_failing_audio.mp4")
# # array = clip.audio.to_soundarray(fps=30)


from moviepy.editor import *
clip2_video = VideoFileClip("ProjectMedia/Clip-1-smash-and-grab.mp4")
changing = clip2_video.cutout(5, 10)  # time is in seconds
print(changing.duration)
changing.write_videofile("original_code127.mp4")
