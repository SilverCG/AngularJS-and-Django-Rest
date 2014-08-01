from django.conf.urls import patterns, url, include 
from api import LeadList

urlpatterns = patterns('',
    url(r'^$', LeadList.as_view(), name='index'),
)

