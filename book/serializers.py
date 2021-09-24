from rest_framework import serializers
from .models import *
from author.models import Author


class ProductRelatedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ("name", "surname", "patronymic", )


class BookSerializer(serializers.ModelSerializer):

    authors = serializers.SlugRelatedField(many=True, read_only=True, slug_field='authors')

    class Meta:
        model = Book
        fields = ['name', "description", "count", "authors"]
        depth = 1