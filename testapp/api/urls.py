from django.urls import path, include

from api import api_views

urlpatterns = [
    path('authors/', api_views.AuthorAPIView.as_view(), name='authors'),
    path('books/', api_views.BookAPIView.as_view(), name='books'),
    path('auth-authors/', api_views.AuthAuthorVIew.as_view(), name='auth-author')
]
