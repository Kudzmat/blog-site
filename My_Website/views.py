from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse


def index(request):
    return HttpResponseRedirect(reverse('Blog:blog_list'))
