from django.db import models


class AdditionalMaterial(models.Model):
    name = models.CharField(max_length=64)
    link = models.URLField(blank=True)
    file = models.FileField(upload_to='courses/lessons/', blank=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'{__class__.__name__}({self.name}, )'


class LessonInfo(models.Model):
    name = models.CharField(blank=True, max_length=256)

    course = models.ForeignKey('mainapp.Course', on_delete=models.CASCADE)
    materials = models.ManyToManyField(AdditionalMaterial)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'{__class__.__name__}({self.name}, )'


class InteractiveLesson(models.Model):
    typing_text = models.TextField(
        verbose_name='Typing text (format: xxxxxx.xxxxxx.xxxxxx)'
    )
    second_limit = models.PositiveSmallIntegerField(null=True)
    error_limit = models.PositiveIntegerField(null=True)

    lesson_info = models.OneToOneField(LessonInfo, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.typing_text[:10]} ...'

    def __repr__(self):
        return f'{__class__.__name__}({self.typing_text}, )'

