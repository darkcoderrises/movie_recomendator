from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'cast/$', views.CastList.as_view()),
    url(r'movie/$', views.MovieList.as_view()),
    url(r'cast/(?P<pk>[0-9]+)/$', views.CastDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
