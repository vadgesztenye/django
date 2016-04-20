from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.json_data_loader, name='jsonloader')
]
