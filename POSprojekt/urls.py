from Core.views import *
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeMain.as_view()),
    path('movie/detail/<str:movie_id>/', ShowMovieDetail.as_view(), name='show_det'),
    path('movie/play/<str:movie_id>/', ShowMovie.as_view(), name='play'),
    path('tag/<int:id>/', ShowTags.as_view(), name='playTag'),
    path('search/', Search.as_view(), name='search'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)