from django.shortcuts import render
from django.http import HttpResponse
from .models import Video

# Create your views here.

def index(request):
    videos = Video.objects.all().order_by('-created_at')
    return render(request, 'vidzine/index.html', {'videos': videos})
