#!/usr/bin/python3

"""
Python script that downloads all the videos from a given youtube playlist
"""

from pytube import Playlist
import sys

pl = Playlist(sys.argv[1])
pl.download_all('/home/gonkaos/Documents/youtube_downloads')
