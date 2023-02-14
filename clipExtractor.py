from moviepy.editor import VideoFileClip

# specify the input video file and start/stop markers
input_video = input("Enter the file path of the video you want to extract a clip from, ex: C:\\Users\Me\SermonFolder\Sermon.mp4\n")
# input_video = r"C:\Users\Gabriel\OneDrive\MBC Folder\29-Gen-Z\29a-Raw Clips\20230101 clips\Clip-1-smash-and-grab.mp4"
start_marker = input("Enter the starting timestamp of the clip you want extracted. Format as hh:mm:ss\n")
stop_marker = input("Enter the ending timestamp of the clip you want extracted. Format as hh:mm:ss\n")
end_file_path = input("Enter the file path for the location you want the clip saved, ex: C:\\Users\Me\SermonFolder\\\n")
clip_name = input("Enter the name of the new clip.\n")

# creating file path of output video
output_video = end_file_path + clip_name

# create a video clip object
clip = VideoFileClip(input_video)

# create a subclip from the specified start and stop markers
subclip = clip.subclip(start_marker, stop_marker)

# specify the output file name and write the subclip
# output_video = r"C:\Users\Gabriel\OneDrive\MBC Folder\29-Gen-Z\PythonExtractorClips\new_clip.mp4"
subclip.write_videofile(output_video)

