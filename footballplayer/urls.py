from django.conf.urls import url
from footballplayer import views

urlpatterns = [
    url(r'^footballplayer/$', views.footballplayer_list)
]
