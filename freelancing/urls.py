"""freelancing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    # path('fileupload',views.fileupload,name='fileupload'),
    path('fileupload_story',views.fileupload_story,name='fileupload_story'),
    path('fileupload_chapter',views.fileupload_chapter,name='fileupload_chapter'),
    path('chapter_page/(?P<s_title>\w+)/',views.chapter_page,name='chapter_page'),
    path('reading_page/(<ss_title>)/(<c_num>)/',views.reading_page,name='reading_page'),
    path('search',views.search,name='search'),
    path('previous/(?P<s_name>\w+)/(?P<c_num>\d+)/',views.previous,name='previous'),
    path('next_chap/(?P<s_name>\w+/(?P<c_num>\d+)/',views.next_chap,name='next_chap'),
    path('add_comment/',views.add_comment,name='add_comment'),
    path('audiobook/',views.audiobook,name='audiobook'),
    path('fileupload_audio/',views.fileupload_audio,name='fileupload_audio'),
    path('fileupload_audio_chapter',views.fileupload_audio_chapter,name='fileupload_audio_chapter'),
    path('audio_chapters/(?P<s_title>\w+)/',views.audio_chapters,name='audio_chapters'),
    path('audio_add_comment/',views.audio_add_comment,name='audio_add_comment'),
  

    
]
urlpatterns +=staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if not settings.DEBUG: urlpatterns += [ path('uploads/(?P<path>.)', serve,{'document_root': settings.MEDIA_ROOT}), path('static/(?P<path>.)/', serve,{'document_root': settings.STATIC_ROOT}), ]