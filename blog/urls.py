from django.urls import path
# import  genriceView
from .views import (
    PostListView,
    PostDetailView,
    # PostCreateView,
    # PostUpdateView,
    # PostDeleteView,
    # UserPostListView
)
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    # path('blog/', views.PostListView.as_view(), name='post_list'),
    path('blog/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='about'),
    path('<int:post_id>/share/',views.post_share, name='post_share'),
    path('blog/', views.post_list, name='post_list'),
    path('<int:year>/<slug:post>/',
        views.post_detail,
        name='post_detail'),
    path('tag/<slug:tag_slug>/',
        views.post_list, name='post_list_by_tag'),     
]
