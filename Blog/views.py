from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, ListView, DetailView, TemplateView, DeleteView
from .models import *
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid


class BlogList(LoginRequiredMixin, ListView):
    context_object_name = 'blogs'
    model = BlogPost
    template_name = 'Blog/blog_list.html'
    queryset = BlogPost.objects.order_by('-publish_date')  # dash is to order by descending order


# class based for creating blog post. It requires user login
class CreateBlog(LoginRequiredMixin, CreateView):
    model = BlogPost
    template_name = 'Blog/create_blog.html'
    fields = ('blog_title', 'blog_content', 'blog_image')

    def form_valid(self, form):
        blog = form.save(commit=False)  # we need to do some edits before saving the blog
        # access current user
        blog.author = self.request.user

        # create slug using title
        title = blog.blog_title

        # replace any spaces in the title with a dash
        # create a unique id for each title , to trail after slug, to avoid issues with duplicate titles
        blog.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())

        # save info
        blog.save()
        return HttpResponseRedirect(reverse('index'))
