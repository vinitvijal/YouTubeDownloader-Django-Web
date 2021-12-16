from django.shortcuts import render
from pytube import YouTube
import os
import shutil
import json

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
    

        if length <= 1200:
            if 'videoMP4' in request.POST:
                videoList = yt.streams.filter(type='video',progressive='True')
                quality = []
                for i in videoList:
                    quality.append(i.resolution)
                number = len(quality)
                print(quality)
                qualityList = json.dumps(quality)
                print(qualityList)
                clean('videos')
                location = "/"
                type = 'Video'
                avail = 'No'



            elif 'audioMP3' in request.POST:
                audioList = yt.streams.filter(type='audio', mime_type='audio/mp4')
                quality = []
                for i in audioList:
                    quality.append(i.abr)
                number = len(quality)
                print(quality)
                qualityList = json.dumps(quality)
                print(qualityList)
                clean('audio')
                audio = yt.streams.get_audio_only()
                location = '/media/audio/' + fileName + '(CodeVinu).mp3'
                type = 'Audio'
                avail = 'No'


            elif 'qualitySelected' in request.POST:
                type = request.POST.get('filetype')
                quality = []
                if type == "Video":
                    List = yt.streams.filter(type='video',progressive='True')
                    for i in List:
                        quality.append(i.resolution)
                elif type == 'Audio':
                    List = yt.streams.filter(type='audio', mime_type='audio/mp4')
                    for i in List:
                        quality.append(i.abr)
                number = len(quality)
                qualityList = json.dumps(quality)
                print(qualityList)
                AudioQuality = request.POST.get('audioQuality')
                VideoQuality = request.POST.get('videoQuality')
                clean('videos')
                if AudioQuality == None and VideoQuality != None:
                    Qual = VideoQuality
                    print(Qual)
                    type = 'Video'
                    video = yt.streams.get_by_resolution(Qual)
                    location = '/media/videos/' + fileName + '(CodeVinu).mp4'
                    video.download(output_path='media/videos/', filename=(fileName + '(CodeVinu).mp4'))
                elif VideoQuality == None and AudioQuality != None:
                    Qual = AudioQuality
                    print(Qual)
                    type = 'Audio'
                    audio = yt.streams.filter(abr=Qual)[0]
                    location = '/media/audio/' + fileName + '(CodeVinu).mp3'
                    audio.download(output_path='media/audio/', filename=(fileName + '(CodeVinu).mp3'))
                avail = 'Yes'




            
            else:
                index(request)

            context = {
                'link': name,
                'type': type,
                'videoName': videoName,
                'location': location,
                "thumbnail": thumbnail,
                'qualityList': qualityList,
                'qualityNum': number,
                'downloadAvail':avail
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
    file = open(path + '/extra.txt', 'w')
    file.write('Hii File')
    file.close()
    

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