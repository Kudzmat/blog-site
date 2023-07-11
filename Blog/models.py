from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    blog_title = models.CharField(max_length=100, verbose_name='Add Title')
    slug = models.SlugField(max_length=200, unique=True)
    blog_content = models.TextField(verbose_name="What's On Your Mind?")
    blog_image = models.ImageField(upload_to='blog_images', verbose_name='Blog Image')
    publish_date = models.DateTimeField(auto_now_add=True)  # automatically adds date when post is published
    update_date = models.DateTimeField(auto_now_add=True)  # to automatically update date after blog updates

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.blog_title


# a comment must be related to a user and a blog post
class Comments(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="blog_comment")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comment")
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-comment_date']  # latest comment will be at the top

    def __str__(self):
        return self.comment


# A like will be linked to a user and a blog post
class Likes(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="liked_blog")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_like")
