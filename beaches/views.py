# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Beach

num_attributes = 6
# Create your views here.

def index(request):
	template = loader.get_template('beaches/index.html')
	return HttpResponse(template.render())

def search(request):
	beaches_list = Beach.objects.order_by('title_text')
	filtered_beaches_list = []
	context = {
		'beaches_list': beaches_list,
		'filtered_beaches_list': filtered_beaches_list,
	}
	return render(request, 'beaches/search.html', context)

def results(request):
	template = loader.get_template('beaches/results.html')

	
	return HttpResponse(template.render())

#def results(request):
