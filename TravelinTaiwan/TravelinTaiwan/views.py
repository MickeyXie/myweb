#-*- coding: utf-8 -*-

from django.shortcuts import render_to_response

def home(request):
	return render_to_response ('home.html')

def general(request):
	return render_to_response ('general.html')

