import json

from django.shortcuts import render
# from .models import Message

from config.settings.base import DJANGO_ROOT
#import django root from the libraries after manage.py
import os


def load_data():
	json_file_path = os.path.join(DJANGO_ROOT,'data','blogs.json')
	with open(json_file_path) as raw_file:
		blog_data = json.load(raw_file)
	return blog_data

def get_post_by_slug(slug):
	for post in blog_data:
		if post['slug'] == slug:
			return post


blog_data = load_data()

def home(request):
	list_of_blogs = {'blogs': blog_data}
	return render(request,'starter_app/home.html', list_of_blogs)


def post(request,slug):
	post = {'post': get_post_by_slug(slug)}
	return render(request,'starter_app/blogs.html', post)

#{} dict
#[] list
