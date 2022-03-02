
from django.shortcuts import render
import requests, random




# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('link')
        print(name)
        if 'instagram.com' in name :
            http = requests.Session()

            def postdownload(cyper):
                req = http.get(f"https://www.instagram.com/p/CL1wvGZnu4I/?__a=1").json()["graphql"]["shortcode_media"][
                    "video_url"]
                req = http.get(req).content
                global context, downName

                downName = 'media/' + str(random.randint(1000000000, 9000000000))+'.mp4'
                with open(downName, 'wb') as f:
                    f.write(req)
                    f.flush()
                    print('Download Successfully, I Love it!!!!')
                    print(downName)
                    context = {
                        'link': name,
                        'location': downName,

                    }
            url = name
            if "reel" in url:
                cod = str(url)
                cyper = (cod[31:42])
                postdownload(cyper)
            elif "tv" in url:
                cod = str(url)
                cyper = (cod[29:40])
                postdownload(cyper)
            elif "p" in url:
                cod = str(url)
                cyper = (cod[28:39])
                postdownload(cyper)
                pass
            return render(request, 'instagram.html', context)

        else:
            print('Else Work')
            return render(request, 'instagram.html')


    return render(request, 'instagram.html')