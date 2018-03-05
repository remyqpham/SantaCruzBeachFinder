from django.conf.urls import url

from . import views

app_name = 'beaches'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'search', views.search, name='search'),
	url(r'results', views.results, name='results'),
	#url pattern for results  e.g. results?
]