"""starter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^$', 'starter.views.home', name='home'),
	url(r'^about/$', 'starter.views.about', name='about'),

	# Auth-related URLs:
	url(r'^accounts/login/$', 'starter.views.login', name='login'),
	url(r'^accounts/process_login/$', 'starter.views.process_login', name='process_login'),
	url(r'^accounts/loggedin/$', 'starter.views.loggedin', name='loggedin'),
	url(r'^accounts/login_error/$', 'starter.views.login_error', name='login_error'),
	url(r'^accounts/logout/$', 'starter.views.logout', name='logout'),
	url(r'^restricted/$', 'starter.views.restricted', name='restricted'),


]
