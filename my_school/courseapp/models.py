from django.db import models

from mainapp.models import Course, AbstractModel


class InteractiveLesson(AbstractModel):
    class Types(models.TextChoices):
        TYPING = 'typing'

    materials = models.TextField(verbose_name='материалы')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


