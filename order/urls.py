from django.urls import path
from .views import *

urlpatterns = [
    path('', get_all, name='order'),
    path('add_order/', add_order, name='add-order'),
    path('<int:pk>/delete_order/', OrderDeleteView.as_view(), name='delete-order'),
    path('<int:pk>/update_order/', OrderUpdateView.as_view(), name='update-order'),
]
