from pytube import YouTube
import sys

link = sys.argv[1]
mp3 = YouTube(link)
mp3 = mp3.streams.filter(only_audio=True).filter(subtype='webm').first()
mp3.download('/home/gonkaos/Documents/youtube_downloads')
