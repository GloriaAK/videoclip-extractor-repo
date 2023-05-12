from moviepy.editor import *
import moviepy.audio.fx.all as afx
video = VideoFileClip("ProjectMedia/Clip-2-I-like-to-sleep.mp4").subclip(0, 75)

music = AudioFileClip('C:\\Users\Gabriel\OneDrive\MBC Folder\\29-Gen-Z\Music\\Tender Full_113_62.mp3').subclip(0, 75).fx(afx.volumex, 0.15).audio_fadein(1).audio_fadeout(1)


# music = AudioFileClip('ProjectMedia/Ardie-45-7.wav')
# music.write_audiofile("Ardie_with_edits3.wav")


naration = video.audio
# naration.write_audiofile("naration3.wav")

audio1 = CompositeAudioClip([naration, music])  # .set_fps(44100)
# audio1.write_audiofile("bgwithvoice3.wav")

final = video.set_audio(audio1).fx(afx.volumex, 3)

final.write_videofile("final_Music_Clip4.mp4", fps=video.fps)
