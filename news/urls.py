from django.urls import path
from news.views import index, about, contact, detail

urlpatterns = [
    path('', index,name='index' ),
    path('about/', about,name='about' ),
    path('contact/', contact,name='contact' ),
    path('<slug:slug>/', detail, name='detail'),
    
    
]