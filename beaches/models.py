# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Beach(models.Model):
	title_text = models.CharField(max_length=100)
	description_text = models.CharField(max_length=2000)
	address_text = models.CharField(max_length=100)
	is_pet_friendly = models.BooleanField(default=False)
	is_alcohol_friendly = models.BooleanField(default=False)
	is_open_after_10pm = models.BooleanField(default=False)
	is_bonfire_friendly = models.BooleanField(default=False)
	is_good_for_surfing = models.BooleanField(default=False)
	has_free_parking = models.BooleanField(default=False)
	photo = models.ImageField(upload_to='beaches')

	def __str__(self):
		return self.title_text