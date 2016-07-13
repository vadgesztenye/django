import json
import os
from django.shortcuts import render
# from .models import Message
from config.settings.base import DJANGO_ROOT
#import django root from the libraries after manage.py
from dateutil import parser
#datetime parser (elemző)



def load_data():
	json_file_path = os.path.join(DJANGO_ROOT,'data','blogs.json')
	
	with open(json_file_path) as raw_file:
		blog_data = json.load(raw_file)
	
	for post_data in blog_data:
		post_data['date'] = parser.parse(post_data['date'])	

	sorted_data = sorted(blog_data, key=lambda k:k['date'], reverse=True)
	
	return sorted_data

def get_post_by_slug(slug):
	for post in blog_data:
		if post['slug'] == slug:
			return post

blog_data = load_data()

def home(request):
	context_dict = {'blogs': blog_data}
	return render(request,'starter_app/home.html', context_dict)


def post(request,slug):
	post = {'post': get_post_by_slug(slug)}
	return render(request,'starter_app/blogs.html', post)

#{} dict
#[] list
