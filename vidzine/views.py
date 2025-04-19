from django.shortcuts import render
from django.http import HttpResponse
from .models import Video
from math import ceil
# Create your views here.

def index(request):
    videos = Video.objects.all().order_by('-created_at')
    return render(request, 'vidzine/index.html', {'videos': videos})
def AllVideos(request):
    allVideo = []
    catVideo = Video.objects.values('category', 'video_id')
    cats = {item['category'] for item in catVideo}
    for cat in cats:
        prod = Video.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        
        allVideo.append([prod, range(1, nSlides), nSlides])

    params = {'allVideo':allVideo}
    return render(request, 'vidzine/Allvideos.html', params)
