#!/usr/bin/python3

from pytube import YouTube
import pyperclip

link = pyperclip.paste()

video = YouTube(link)

download = video.streams.first().download(
    '/home/gonkaos/Documents/youtube_downloads'
)
