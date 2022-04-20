import shutil
from urllib import request
from django.shortcuts import render
import requests
import random
import os
from instagrapi import Client

cl = Client()


def instaPost(url, typeOfData):
    print(url)
    parent_dir = os.path.dirname(os.path.abspath('manage.py'))
    main_dir = parent_dir + '/media'
    path = os.path.join(main_dir, 'instaDown')
    cl.login('ritikaraturi0812', '19122002')



    if typeOfData == 2:
        local_file = str(random.randrange(10000000,900000000))+'-(CodeVinu).mp4'

    elif typeOfData == 1:
        local_file = str(random.randrange(10000000,900000000))+'-(CodeVinu).jpeg'


    else:
        index(request)
    
    os.chdir(path)
    data = requests.get(url)

    with open(local_file, 'wb')as file:
        file.write(data.content)
        print('\nDownloaded Successfully!!!')
    os.chdir(parent_dir)
    return local_file


def clean(folder='insta'):
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


# Create your views here.
def index(request):
    if request.method == 'POST':
        typeOfData = request.POST.get('Post')
        link = request.POST.get('link')
        print(typeOfData)
        print(link)
        if typeOfData == 'Post':
            pk = cl.media_pk_from_url(link)
            print(pk)
            data = cl.media_info(pk).dict()
            mediatype = data['media_type']
            if mediatype == 2:
                video_url = cl.media_info_gql(pk).video_url
                print(video_url)
                filename = instaPost(video_url, mediatype)
                location = '/media/instaDown/' + filename
        context = {
            'downloadLink': location,
        }
        return render(request, 'insta.html', context=context)




    else:

        return render(request, 'insta.html')
    return render(request, 'insta.html')