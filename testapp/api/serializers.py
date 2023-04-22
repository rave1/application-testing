from rest_framework import serializers
from api.models import Book, Author
from django.contrib.auth import get_user_model


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = (
            'id', 'first_name', 'last_name'
        )


class BookSerializer(serializers.ModelSerializer):

    author_name = serializers.CharField(source='author.display_name', read_only=True)

    class Meta:
        model = Book
        fields = (
            'id', 'title', 'description', 'author_name',
            'genre', 'publish_date', 'author'
        )
        extra_kwargs = {
            'author': {'write_only': True}
        }


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = (
            'id', 'username', 'email', 'last_login'
        )
