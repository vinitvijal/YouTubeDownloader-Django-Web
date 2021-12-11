from django.shortcuts import render
from pytube import YouTube

# Create your views here.
def index(request):
    if request.method =='POST':
        name = request.POST.get('link')
        print(name)
        yt = YouTube(name)
        videoName = yt.title
        print(videoName)
        context = {
            'videoName': videoName
        }
        return render(request, 'index.html', context)
    else:

        return render(request, 'index.html')





