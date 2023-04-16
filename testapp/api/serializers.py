from rest_framework import serializers
from api.models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = (
            'id', 'first_name', 'last_name'
        )


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = (
            'id', 'title', 'description', 'author',
            'genre', 'publish_date'
        )
