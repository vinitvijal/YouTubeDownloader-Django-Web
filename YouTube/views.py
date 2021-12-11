from django.shortcuts import render
from pytube import YouTube

# Create your views here.
def index(request):
    if request.method =='POST' and 'verify' in request.POST:
        name = request.POST.get('link')
        print(name)
        yt = YouTube(name)
        videoName = yt.title
        fileName = videoName.replace(' ','_')
        print(videoName)
        print()
        stream = yt.streams.filter(progressive=True)
        for i in stream:
            print(i, end='\n\n')
        video = yt.streams.get_highest_resolution()



        location = '/static/videos/' + fileName + '.mp4'

        video.download(output_path='static/videos/', filename=(fileName + '.mp4'))




        context = {
            'videoName': videoName,
            'location': location
        }
        return render(request, 'index.html', context)
    # elif request.method =='POST' and 'download' in request.POST:
    #     print("Button Working")
    #
    #     yt = YouTube(name)
    #
    #     print(yt.title)
    #     print()
    #     stream = yt.streams.filter(progressive=True)
    #
    #     for i in stream:
    #         print(i, end='\n\n')
    #
    #     video = yt.streams.get_highest_resolution()
    #     video.download()
    #     return render(request, 'index.html', context)

    else:

        return render(request, 'index.html')



def rename(fileName):
    fileList = fileName.replace(' ', '_')
    print(fileList)


