from django.urls import path
from .views import *

urlpatterns = [
    path('', creat_user, name='create_user')
]
