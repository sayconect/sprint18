from django.urls import path
from .views import *

urlpatterns = [
    path('', get_all, name='book'),
    path('add_book/', add_book, name = 'add_book'),
    path('<int:book_id>/', book_by_id, name='book_by_id'),
    path('<int:pk>/update/', BookUpdateViews.as_view(), name='update_book'),
    path('<int:book_id>/delete', delete_book, name='delete_book'),
    path('api/v1/book', BookAPIView.as_view()),
]
