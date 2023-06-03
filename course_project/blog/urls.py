from django.urls import path
from .views import CreateBlogView, BlogDetailView, BlogListView, UpdateBlogView, DeleteBlogView, delete_blog



urlpatterns = [
    path('bloqlar/', BlogListView.as_view(), name='blogs'),
    path('bloqlar/yarat', CreateBlogView.as_view(), name='blog_create'),
    path('bloqlar/<slug:slug>', BlogDetailView.as_view(), name='blog_detail'),
    path('bloqlar/duzelis/<slug:slug>', UpdateBlogView.as_view(), name='blog_update'),
    path('bloqlar/sil/<slug:slug>', delete_blog, name='blog_delete'),
]
