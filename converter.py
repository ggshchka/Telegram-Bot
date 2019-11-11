# -*- coding: utf-8 -*-
import youtube_dl
import os

def convert(url):
	dirName = 'mp3'
	if not os.path.exists(dirName):
		os.mkdir(dirName)
	options = {
		'outtmpl': unicode('./mp3/%(title)s.%(ext)s'),
	    'format': 'bestaudio/best',
	    'postprocessors': [{
	        'key': 'FFmpegExtractAudio',
	        'preferredcodec': 'mp3',
	        'preferredquality': '192',
	    }],
	}      
	try:
		title = os.listdir("./mp3")
		with youtube_dl.YoutubeDL(options) as ydl:
			info = ydl.extract_info(url, download=True)
			nm = ydl.prepare_filename(info)   # get /mp3/filename.webm
			mp3_file = nm[:-4] + 'mp3'		  # get /mp3/filename.mp3
			return mp3_file
	except:
		return 'UrlError'

def delete(audio):
	os.remove(audio)