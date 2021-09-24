from rest_framework import serializers
from .models import *


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'user', "book", "created_at", "end_at", "plated_end_at", ]
        depth = 1