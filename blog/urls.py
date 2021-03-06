from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
 
urlpatterns = [
    path('',PostListView.as_view(),name='blog-home'),
    path('post/<int:pk>/',PostDetailView.as_view(),name ='post-detail'),
    # path('postComment',views.PostComment,name='postComment'),
    path('post/new_post/',PostCreateView.as_view(),name ='post-create'),
    path('post/<int:pk>/update_post/',PostUpdateView.as_view(),name ='post-update'),
    path('post/<int:pk>/delete_post/',PostDeleteView.as_view(),name ='post-delete'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('about/',views.about,name='blog-about'),
    path('dashboard/',views.dashboard,name='dashboard')
   


]