# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 13:06:37 2022

@author: Saurabh kumar
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 12:41:56 2022

@author: Saurabh kumar
"""

# install ------pip install pytube

from pytube import YouTube

link= "https://www.youtube.com/watch?v=iCRh1IGw5wI"
youtube_1= YouTube(link)

#print(youtube_1.title)
#print(youtube_1.thumbnail_url)
videos= youtube_1.streams.filter(only_audio=True) # for audio use only_audio otherwise wanna download video remove only_audio
vid= list(enumerate(videos))
for i in vid:
    print(i)
print()
strm= int(input('enter:'))
videos[strm].download()
print('successfully downloaded')

