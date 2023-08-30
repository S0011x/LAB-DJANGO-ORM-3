from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    path('posts/', views.posts, name='posts'),
    path('add_post/', views.add_post, name='add_post'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/update/', views.post_update, name='post_update'),
    path('post/<int:post_id>/delete/', views.post_delete, name='post_delete'),
    path("all/", views.all_posts, name="all_posts"),
    path('search/', views.search, name='search'),
    
]