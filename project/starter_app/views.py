import json

from django.shortcuts import render
# from .models import Message

from config.settings.base import DJANGO_ROOT
#import django root from the libraries after manage.py
import os

json_file_path = os.path.join(DJANGO_ROOT,"data","blogs.json")

with open(json_file_path) as raw_file:
	loaded_file = json.load(raw_file)
	raw_file.close()

def json_data_loader(request):
	list_of_blogs = {"blogs": loaded_file}
	return render(request,"starter_app/home.html", list_of_blogs)

