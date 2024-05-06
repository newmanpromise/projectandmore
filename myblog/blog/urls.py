
from django.urls import path, include
from .views import Homeview, ArtileDetailview

urlpatterns = [
    path('', Homeview.as_view(), name='home'),
    path('article/<int:pk>', ArtileDetailview.as_view(), name='article-detail'),
]