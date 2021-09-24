from rest_framework import serializers
from .models import *
from author.models import Author


class AuthorRelatedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ("id", "name", "surname", "patronymic", )


class BookSerializer(serializers.ModelSerializer):

    authors = serializers.SlugRelatedField(many=True, read_only=True, slug_field='authors')

    class Meta:
        model = Book
        fields = ['id', 'name', "description", "count", "authors"]
        depth = 1