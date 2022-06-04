from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField()

    def __str__(self):
        return self.name + " " + self.last_name


GENRE = {
    (0, 'Action and Adventure'),
    (1, 'Classics'),
    (1, 'Fantasy'),
    (2, 'Science Fiction'),
    (3, 'Horror/Thriller'),
    (4, 'Romance'),
    (5, 'Biography'),

}


class Book(models.Model):
    title = models.CharField(max_length=50)
    models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateField()
    genre = models.PositiveSmallIntegerField(default=0, choices=GENRE)

    def __str__(self):
        return self.title



