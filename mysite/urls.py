from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('scramble/', include('scramble.urls')),
    path('chat/', include('chat.urls')),
    path('Call/', include('OneToOneCallChat.urls')),
    path('account/', include('UserHandle.urls')),
    path('admin/', admin.site.urls),
    path("home", views.home, name="home"),
    path("about", views.about, name="about"),
    path("contactus", views.contactus, name="contactus"),
    
]
