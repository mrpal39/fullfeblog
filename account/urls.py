from django.urls import path
from . import views
# Create your tests here.
urlpatterns = [
# ...
path('users/', views.user_list, name='user_list'),
path('users/<username>/', views.user_detail, name='user_detail'),
path('users/follow/', views.user_follow, name='user_follow'),
]