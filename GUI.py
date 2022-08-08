from tkinter.filedialog import askopenfilename
from calendar import c
from tkinter import messagebox
from pytube import YouTube
import PySimpleGUI as psg
from PySimpleGUI import *
import moviepy.editor


psg.theme('DarkGray2')
layout = [
    [psg.Image(source="d1.png")],
    [psg.Text('Coloque o link do video para Download.'), psg.Input(key='site')],
    [psg.Button('Baixar'), psg.Button('Converter')],
    

]
window = psg.Window('YoutubeDownloader', layout=layout, element_justification='c')

while True:
   
   eventos, valores = window.read()

   if eventos == psg.WINDOW_CLOSED:
    break
   if eventos == 'Baixar':
    if valores['site']:
        site = valores['site']
        yt = YouTube(site)
        yt.streams.get_highest_resolution().download()
   if eventos == 'Converter':
        video = askopenfilename()     
        video = moviepy.editor.VideoFileClip(video)
        som = video.audio
        som.write_audiofile("music.mp3")
   


   