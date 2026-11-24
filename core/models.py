from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    isbn = models.CharField(max_length=20, unique=True)
    category = models.CharField(max_length=100)
    publication_year = models.PositiveIntegerField()
    availability = models.CharField(
        max_length=20,
        choices=[
            ('available', 'Available'),
            ('borrowed', 'Borrowed'),
        ],
        default='available',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
