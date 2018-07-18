#!/usr/bin/python3

from pytube import YouTube
import sys

link = sys.argv[1]

video = YouTube(link)

download = video.streams.first().download(
    '/home/gonkaos/Documents/youtube_downloads'
)
