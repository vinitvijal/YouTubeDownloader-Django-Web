from django.shortcuts import render

def playlist(request):
    return render(request, "playlist.html")