from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250, null=False)
    slug = models.SlugField()
    excerpt = models.CharField(max_length=160, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    body = models.TextField()
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return self.title
