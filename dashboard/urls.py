from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^mockdata', views.mockDualSeries, name='mockData'),
    url(r'^$', views.index, name='home')
)
