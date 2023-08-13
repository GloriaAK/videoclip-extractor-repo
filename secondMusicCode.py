from moviepy.editor import *
import moviepy.audio.fx.all as afx
# video = VideoFileClip("ProjectMedia/Clip-2-I-like-to-sleep.mp4").subclip(0, 75)
#
# music = AudioFileClip('C:\\Users\Gabriel\OneDrive\MBC Folder\\29-Gen-Z\Music\\Tender Full_113_62.mp3').subclip(0, 75).fx(afx.volumex, 0.15).audio_fadein(1).audio_fadeout(1)
#
#
# # music = AudioFileClip('ProjectMedia/Ardie-45-7.wav')
# # music.write_audiofile("Ardie_with_edits3.wav")
#
#
# naration = video.audio
# # naration.write_audiofile("naration3.wav")
#
# audio1 = CompositeAudioClip([naration, music])  # .set_fps(44100)
# # audio1.write_audiofile("bgwithvoice3.wav")
#
# final = video.set_audio(audio1).fx(afx.volumex, 3)
#
# final.write_videofile("final_Music_Clip4.mp4", fps=video.fps)
"""This is the independent music clipping section of Future GUI"""
music_filepath = "C:\\Users\\kluth_1eiw4u3\\OneDrive\\MBC Folder\\29-Gen-Z\\Music\\Light of Men - TDRC.mp3"
starting_string = "0:35:50"
ending_string = "0:36:31"
point_of_emphasis = "0:36:04"
if "Tender Heart" in music_filepath:
    music_point_of_emphasis = 62
elif "Unity of the Spirit" in music_filepath:
    music_point_of_emphasis = 25
elif "Take Up Your Cross" in music_filepath:
    music_point_of_emphasis = 65
elif "Renewal" in music_filepath:
    music_point_of_emphasis = 64
elif "Rejoice in the Morning" in music_filepath:
    music_point_of_emphasis = 45
elif "Light of Men" in music_filepath:
    music_point_of_emphasis = 86

start_sec1 = starting_string[-2:]
start_min1 = starting_string[-5:-3]

end_sec1 = ending_string[-2:]
end_min1 = ending_string[-5:-3]

mid_sec1 = point_of_emphasis[-2:]
mid_min = point_of_emphasis[-5:-3]

m_duration = int(end_min1) - int(start_min1)
if (int(end_min1) - int(start_min1)) <= 0:
    print("Subclip within the minute")
    s_duration = (int(end_sec1)) - (int(start_sec1))
    total_duration = ((m_duration * 60) + (s_duration))
else:
    print("Subclip more than a minute")
    s_duration = (60 - (int(start_sec1))) + (int(end_sec1))
    total_duration = (m_duration * 60) + (s_duration)-60

print("{} is the total duration in seconds".format(total_duration))

m_duration = int(mid_min) - int(start_min1)
if (int(mid_min) - int(start_min1)) <= 0:
    print("Seconds until POE within a minute")
    s_duration = (int(mid_sec1)) - (int(start_sec1))
    duration_until_POE = ((m_duration * 60) + (s_duration))
else:
    print("Seconds until POE more than a minute")
    s_duration = (60 - (int(start_sec1))) + (int(mid_sec1))
    duration_until_POE = (m_duration * 60) + (s_duration)-60

print("{} is the number of seconds until the point of emphasis".format(duration_until_POE))

duration_after_POE = total_duration - duration_until_POE

time_start = music_point_of_emphasis - duration_until_POE
time_end = music_point_of_emphasis + duration_after_POE

music = AudioFileClip(music_filepath).subclip(time_start, time_end)
music_audio_dynamics = music.fx(afx.volumex, 0.5).audio_fadein(1).audio_fadeout(1)
music_audio_dynamics.write_audiofile("C:\\Users\\kluth_1eiw4u3\\OneDrive\\MBC Folder\\29-Gen-Z\\Music\\L_Music5.mp3")

