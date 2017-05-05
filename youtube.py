from __future__ import unicode_literals
import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=cHOrHGpL4u0&index=4&list=RD1seDBXvGYcc'])
    
                  


'''#find format
options = {
    'format': 'bestaudio/best',  # choice of quality
    'extractaudio': True,        # only keep the audio
    'audioformat': "mp3",        # convert to mp3
    'outtmpl': '%(id)s',         # name the file the ID of the video
    'noplaylist': True,          # only download single song, not playlist
    'listformats': True,         # print a list of the formats to stdout and exit
}

with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=1seDBXvGYcc'])'''
