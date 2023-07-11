from django.urls import path, include
from . import views

app_name = 'Blog'

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('create-blog/', views.CreateBlog.as_view(), name='create_blog'),
    path('post/<str:slug>/', views.read_post, name='read_post'),
    path('my-blogs/', views.MyBlogs.as_view(), name='my_blogs'),
    path('edit-blog/<pk>/', views.EditBlog.as_view(), name='edit_blog')  # pk is primary key

]
