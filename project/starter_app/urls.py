from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^/post(?P<slug>[\w-]+)/$', views.post, name='post')
]
