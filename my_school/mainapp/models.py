from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'{__class__.__name__}({self.name})'


class Course(models.Model):

    class Levels(models.TextChoices):
        EASY = 1
        NORMAL = 2
        HARD = 3

    name = models.CharField(
        max_length=512,
        unique=True
    )
    description = models.TextField()
    img = models.ImageField(upload_to='courses/photo/')
    price = models.IntegerField()
    level = models.CharField(
        max_length=1,
        choices=Levels.choices,
        default=Levels.EASY
    )
    date = models.DateField(
        auto_created=True,
        verbose_name='date of creation'
    )

    authors = models.ManyToManyField('authapp.SchoolUser', related_name='authors')
    students = models.ManyToManyField('authapp.SchoolUser', related_name='students', blank=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{__class__.__name__}({self.name}, )'
