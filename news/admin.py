from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    class Meta:
        model = Post
        
    list_display = [
        'title',
        'author',
        'created_at',
    ]
    
    prepopulated_fields = {
        'slug': ('title',)  
    }
    
admin.site.register(Post, PostAdmin)