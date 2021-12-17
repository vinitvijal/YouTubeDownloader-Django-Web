from django.shortcuts import render


# Create your views here.
def adless(request):
    if request.method == "POST":
        link = request.POST.get('link')
        print(link)
        
        

    
    return render(request, 'adless.html')
