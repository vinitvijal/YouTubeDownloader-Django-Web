import shutil
from urllib import request
from django.shortcuts import render
import requests
import random
import os

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0'}

def instaPost(linkSlice):
    url = ((linkSlice)+'/?__a=1')
    print(url)
    data = requests.get(url, headers=headers)

    if data.status_code == 200:
        print("valid")
    jsonData = data.json()
    if jsonData['graphql']['shortcode_media']['__typename'] == 'GraphVideo':
        local_file = str(random.randrange(10000000,900000000))+' - (CodeVinu).mp4'
        downlink = jsonData['graphql']['shortcode_media']['video_url']

    elif jsonData['graphql']['shortcode_media']['__typename'] == 'GraphImage':
        local_file = str(random.randrange(10000000,900000000))+' - (CodeVinu).jpeg'
        list_of_sources = jsonData['graphql']['shortcode_media']['display_resources']
        downlink = list_of_sources[-1]['src']

    else:
        index(request)
    
    os.chdir('media/instaDown')
    data = requests.get(downlink)

    with open(local_file, 'wb')as file:
        file.write(data.content)
        print('\nDownloaded Successfully!!!')
    os.chdir('../../')


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


# Create your views here.
def index(request):
    if request.method == 'POST':
        typeOfData = request.POST.get('Post')
        link = request.POST.get('link')
        print(typeOfData)
        print(link)
        if typeOfData == 'Post':
            if link[26] == 'p':
                linkSlice = link[0:39]
                # Main Json and Download Section
                instaPost(linkSlice)
                
    else:

        return render(request, 'insta.html')
    return render(request, 'insta.html')