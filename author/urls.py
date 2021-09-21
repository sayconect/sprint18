from django.urls import path
from .views import *

urlpatterns = [
    path('', get_all, name='author'),
    path('add_author/', add_author, name='add-author'),
    path('<int:pk>/', AuthorDetailView.as_view(), name='author-details'),
    path('<int:pk>/update/', AuthorUpdateView.as_view(), name='author-update'),
path('<int:pk>/delete/', AuthorDeleteView.as_view(), name='author-delete'),
]
