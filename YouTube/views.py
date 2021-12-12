from django.shortcuts import render
from pytube import YouTube

# Create your views here.
def index(request):
    if request.method =='POST':
        name = request.POST.get('link')
        print(name)
        yt = YouTube(name)
        videoName = yt.title
        fileName = (videoName.replace(' ' ,'_')).replace('|','-')
        print(videoName)
        print()
        stream = yt.streams.filter(type='audio')
        for i in stream:
            print(i, end='\n\n')
        if 'videoMP4' in request.POST:
            video = yt.streams.get_highest_resolution()
            location = '/media/videos/' + fileName + '.mp4'
            video.download(output_path='media/videos/', filename=(fileName + '.mp4'))

        elif 'audioMP3' in request.POST:
            audio = yt.streams.get_audio_only()
            location = '/media/audio/' + fileName + '.mp3'
            audio.download(output_path='media/audio/', filename=(fileName + '.mp3'))
        else:
            index(request)

        context = {
            'videoName': videoName,
            'location': location
        }
        return render(request, 'index.html', context)

    else:

        return render(request, 'index.html')




