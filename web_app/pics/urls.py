from django.conf.urls import url
from . import views

app_name = 'pics'

urlpatterns = [
    # /pics/
    url(r'^$', views.index, name='index'),

    # /pics/<album_id>/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    # /pics/favorite
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite')
]