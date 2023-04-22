from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=32)

    @property
    def display_name(self) -> str:
        return f'{self.first_name} {self.last_name}'

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):

    ACTION = 'A'
    SCIFI = 'S'
    THRILLER = 'T'

    GENRE_CHOCIES = [
        (ACTION, 'Action'),
        (SCIFI, 'Sci-fi'),
        (THRILLER, 'Thriller')
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    publish_date = models.DateField()
    genre = models.CharField(choices=GENRE_CHOCIES, max_length=1, default=ACTION)
