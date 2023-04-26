from moviepy.editor import *
video_start = "0:32:20"
video_end = "0:32:23"
clip1 = ImageClip("ProjectMedia/green_back.png").subclip(video_start, video_end)
new_clips = VideoFileClip("C:\\Users\\Gabriel\\OneDrive\\MBC Folder\\21-Broadcast\\21f-Raw Sermon Video\\Pay Attention To Last Words.mp4").subclip(video_start, video_end)
old_clips = VideoFileClip("ProjectMedia\Clip-1-smash-and-grab.mp4").subclip("0:00:01", "0:00:04")
clip3 = ImageClip("ProjectMedia/green_back.png").subclip(video_start, video_end)
ender_clip = ImageClip("ProjectMedia/green_final.png").subclip("0:00:00", "0:00:02")
# when y2=less, img=less: for clip2, when x1=more, left side cuts more, when x2=more, right side cuts less:

if round(old_clips.fps, 3) == 20.000:
    resized_clip1 = clip1.crop(x1=0, x2=0, y1=0, y2=540)
    resized_clip2 = new_clips.crop(x1=160, x2=1120, y1=0, y2=0).resize(1.125)
    resized_clip3 = clip3.crop(x1=0, x2=0, y1=1380, y2=0)
elif round(old_clips.fps, 3) == 23.976:
    resized_clip1 = clip1.crop(x1=0, x2=0, y1=0, y2=540)
    resized_clip2 = new_clips.crop(x1=120, x2=840, y1=0, y2=0).resize(1.5)
    resized_clip3 = clip3.crop(x1=0, x2=0, y1=1380, y2=0)
else:
    print("Something is wrong")
# print(clip2.fps)
# print(round(clip__2.fps, 3))
# resized_clip1 = clip1.crop(x1=0, x2=0, y1=0, y2=540)
# resized_clip2 = clip2.crop(x1=120, x2=840, y1=0, y2=0).resize(1.5)
# resized_clip3 = clip3.crop(x1=0, x2=0, y1=1380, y2=0)

# resized_clip1 = clip1.crop(x1=0, x2=0, y1=0, y2=540)
# resized_clip2 = clip2.crop(x1=160, x2=1120, y1=0, y2=0).resize(1.125)
# resized_clip3 = clip3.crop(x1=0, x2=0, y1=1380, y2=0)

adding_clips = clips_array([[resized_clip1], [resized_clip2], [resized_clip3]])
body = adding_clips.resize((1080, 1920))


final_clip = concatenate_videoclips([body, ender_clip])
final_clip.write_videofile("resize_testing5.mp4")
