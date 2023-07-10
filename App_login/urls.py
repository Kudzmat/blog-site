from django.urls import path, include
from . import views

app_name = 'App_login'

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile_page, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('password/', views.change_password, name='change_password'),
    path('add-profile-image/', views.add_profile_pic, name='add_profile_pic'),
    path('update-profile-image/', views.update_profile_pic, name='update_profile_pic')

]
