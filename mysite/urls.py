from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views
from . import settings
from django.conf.urls.static import static

urlpatterns = [
	path('scramble/', include('scramble.urls')),
	path('music/', include('music_nation.urls')),
    path('chat/', include('chat.urls')),
    path('Call/', include('OneToOneCallChat.urls')),
    path('account/', include('UserHandle.urls')),
    path('admin/', admin.site.urls),
    path("home", views.home, name="home"),
    path("about", views.about, name="about"),
    path("contactus", views.contactus, name="contactus"),
    path("tictactoe", views.tictactoe, name="tictactoe")
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
