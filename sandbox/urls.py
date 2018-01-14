from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import (
    include, path
)

from .views import (
    HomeView, PostListView, PostDetailView, PostCreateView
)

urlpatterns = [
    path('',
         HomeView.as_view(), name='home'),

    path('posts',
         PostListView.as_view(), name='post-list'),

    path('posts/<int:pk>',
         PostDetailView.as_view(), name='post-detail'),

    path('posts/create',
         PostCreateView.as_view(), name='post-create'),

    path('posts/update/<int:pk>',
         PostDetailView.as_view(), name='post-update'),

    path('posts/delete/<int:pk>',
         PostDetailView.as_view(), name='post-delete'),

    path('jfu2/',
         include('jfu2.urls', namespace='jfu')),

    path('admin/',
         admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
