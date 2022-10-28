from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("blog/", views.BlogListView.as_view(), name="blog_list_view"),
    path('blog/<str:pk>/', views.BlogDetailView.as_view(), name='blog_detail_view'),
    path('blog-create/', views.BlogCreateView.as_view(), name='blog_create_view'),
    path('my-blog/', views.MyBlogListView.as_view(), name='my_blog_list_view'),
]
