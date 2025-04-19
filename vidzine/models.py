from django.db import models

# Create your models here.

class Video(models.Model):
    video_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200, default='all')
    description = models.TextField(blank=True)
    video_file = models.FileField(upload_to='videos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title