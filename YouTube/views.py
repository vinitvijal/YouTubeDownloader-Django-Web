from django.shortcuts import render
from pytube import YouTube
import os
import shutil

# Create your views here.
def index(request):
    if request.method =='POST':
        name = request.POST.get('link')
        print(name)
        yt = YouTube(name)
        videoName = yt.title
        length = yt.length

        audioStream = yt.streams.filter(type='audio', abr='128kbps')[0].url
        print("audio = \n", audioStream, '\n\n')
        videoStream = yt.streams.filter(progressive='true')[-1].url
        print("video = \n", videoStream, '\n\n')
        fileName = nameConverter(videoName)
        print(videoName)
        print()
        thumbnail = yt.thumbnail_url
        stream = yt.streams.filter(type='audio')
        for i in stream:
            print(i, end='\n\n')

        if length <= 1200:
            if 'videoMP4' in request.POST:
                clean('videos')
                video = yt.streams.get_highest_resolution()
                location = '/media/videos/' + fileName + '(CodeVinu).mp4'
                video.download(output_path='media/videos/', filename=(fileName + '(CodeVinu).mp4'))
                type = 'Video'

            elif 'audioMP3' in request.POST:
                clean('audio')
                audio = yt.streams.get_audio_only()
                location = '/media/audio/' + fileName + '(CodeVinu).mp3'
                audio.download(output_path='media/audio/', filename=(fileName + '(CodeVinu).mp3'))
                type = 'Audio'
            else:
                index(request)

            context = {
                'type': type,
                'videoName': videoName,
                'location': location,
                "thumbnail": thumbnail
            }
            return render(request, 'index.html', context)
        else:

            if 'videoMP4' in request.POST:
                location = videoStream

            elif 'audioMP3' in request.POST:
                location = audioStream
            context = {
                'Disclamer': "Hii",
                "videoName": videoName,
                'location': location,
            }
            return render(request, 'index.html', context)

    else:

        return render(request, 'index.html')


def clean(folder='audio'):
    directory = folder
    parent_dir = os.path.dirname(os.path.abspath('manage.py'))+'/media'
    print(parent_dir)
    # Removing Folders
    path = os.path.join(parent_dir, directory)
    shutil.rmtree(path)
    # Create Folders
    os.mkdir(path)

    print("Media Data is Cleared!!!!")

def nameConverter(title):
    a = title
    z = []

    for i in a:
        if i.isalnum():
            z.append(i)
        elif i == " ":
            z.append('_')
        elif i == "|":
            z.append('-')
        else:
            z.append('_')

    newTitle = ''.join(z)
    return newTitle