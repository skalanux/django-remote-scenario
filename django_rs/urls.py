from django.conf.urls import url

from django_rs import views


urlpatterns = [
    url(r'^$', views.index, name='index')
]
