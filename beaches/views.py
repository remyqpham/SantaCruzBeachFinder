# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.template.defaulttags import register

from .models import Beach

import urlparse

num_attributes = 6

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

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
	#template = loader.get_template('beaches/results.html')
	beaches_list = Beach.objects.order_by('title_text')
	filtered_beaches_list = Beach.objects.order_by('title_text')
	filtered_beaches_photos_urls = {}
	filtered_beaches_desc_previews = {}

	is_pet_friendly = request.GET['is_pet_friendly']
	is_alcohol_friendly = request.GET['is_alcohol_friendly']
	is_open_after_sunset = request.GET['is_open_after_sunset']
	is_bonfire_friendly = request.GET['is_bonfire_friendly']
	is_camping_friendly = request.GET['is_camping_friendly']
	is_good_for_surfing = request.GET['is_good_for_surfing']
	has_free_parking = request.GET['has_free_parking']

	if is_pet_friendly=='1':
		filtered_beaches_list = filtered_beaches_list.filter(is_pet_friendly=True)
	if is_alcohol_friendly=='1':
		filtered_beaches_list = filtered_beaches_list.filter(is_alcohol_friendly=True)
	if is_open_after_sunset=='1':
		filtered_beaches_list = filtered_beaches_list.filter(is_open_after_sunset=True)
	if is_bonfire_friendly=='1':
		filtered_beaches_list = filtered_beaches_list.filter(is_bonfire_friendly=True)
	if is_camping_friendly=='1':
		filtered_beaches_list = filtered_beaches_list.filter(is_camping_friendly=True)
	if is_good_for_surfing=='1': 
		filtered_beaches_list = filtered_beaches_list.filter(is_good_for_surfing=True)
	if has_free_parking=='1':
		filtered_beaches_list = filtered_beaches_list.filter(has_free_parking=True)

	filtered_beaches_list = filtered_beaches_list.order_by('title_text')

	for beach in filtered_beaches_list:
		photoURL = str(beach.photo.url)
		filtered_beaches_photos_urls[beach.id] = photoURL[7:]
		desc = beach.description_text
		filtered_beaches_desc_previews[beach.id] = desc[0:150]


	context = {
		'request': request,
		'beaches_list':beaches_list,
		'filtered_beaches_list':filtered_beaches_list,
		'is_pet_friendly':is_pet_friendly,
		'is_alcohol_friendly':is_alcohol_friendly,
		'is_open_after_sunset':is_open_after_sunset,
		'is_bonfire_friendly':is_bonfire_friendly,
		'is_camping_friendly':is_camping_friendly,
		'is_good_for_surfing':is_good_for_surfing,
		'has_free_parking':has_free_parking,
		'filtered_beaches_photos_urls':filtered_beaches_photos_urls,
		'filtered_beaches_desc_previews':filtered_beaches_desc_previews,
	}
	return render(request, 'beaches/results.html', context)

def details(request, beach_id):
	beaches_list = Beach.objects.order_by('title_text')
	try:
		beach = beaches_list.get(pk=beach_id)
	except Beach.DoesNotExist:
		raise Http404("Beach does not exist.")
	photo = beach.photo
	photoURL = str(beach.photo.url)
	photoURL = photoURL[7:]
	context = {
		'beach_id':beach_id,
		'beach':beach,
		'photo':photo,
		'photoURL':photoURL,
	}
	return render(request, 'beaches/details.html', context)
