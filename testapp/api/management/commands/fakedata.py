from django.core.management.base import BaseCommand, CommandError
from api.models import Author, Book
from typing import Any, Optional
from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help = 'fakedata for test app'

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        for i in range(20):
            Author.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name()
            )
        self.stdout.write('Authors created')

        for author in Author.objects.all():
            for i in range(5):
                Book.objects.create(
                    author=author,
                    title=fake.sentence(nb_words=4),
                    description=fake.paragraph(nb_sentences=3),
                    publish_date=fake.date(),
                    genre=fake.random_element(elements=('A', 'S', 'T'))
                )
        self.stdout.write('books created')
