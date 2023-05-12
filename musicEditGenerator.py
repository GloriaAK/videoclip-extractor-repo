# this takes in a full length music clip and cuts it into short clips and names them accordingly.
# the first number is length in seconds and the second is length of time until point of emphasis
from moviepy.editor import *
import moviepy.audio.fx.all as afx
# music = AudioFileClip('C:\\Users\Gabriel\OneDrive\MBC Folder\\29-Gen-Z\Music\\Tender Full_113_62.mp3').subclip(0, 75)
# music_audio_dynamics = music.fx(afx.volumex, 0.15).audio_fadein(1).audio_fadeout(1)
# music_audio_dynamics.write_audiofile("Tender{}_{}.wav".format(30, cut_2))
# C:\Users\Gabriel\OneDrive\MBC Folder\29-Gen-Z\Music\TenderMusic



for i in range(37, 58):
    music = AudioFileClip('C:\\Users\Gabriel\OneDrive\MBC Folder\\29-Gen-Z\Music\\The David Roy Collective - A Tender Heart.wav').subclip(i, i+30)
    music_audio_dynamics = music.fx(afx.volumex, 0.15).audio_fadein(1).audio_fadeout(1)
    music_audio_dynamics.write_audiofile("C:\\Users\\Gabriel\\OneDrive\\MBC Folder\\29-Gen-Z\\Music\\TenderMusic\\Tender{}_{}.mp3".format(30, 62-i))



