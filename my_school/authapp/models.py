from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class SchoolUser(AbstractUser):

    class Sexes(models.TextChoices):
        MALE = 'm', _('Man')
        FEMALE = 'f', _('Woman')

    avatar = models.ImageField(upload_to='users/photo/', blank=True)
    birth_date = models.DateField(null=True)
    sex = models.CharField(choices=Sexes.choices, max_length=1)
    about_me = models.TextField(blank=True)

    tags = models.ManyToManyField('mainapp.Tag', blank=True)

    @property
    def avatar_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        return '/static/img/person-circle-outline.svg'

    def __str__(self):
        return self.get_full_name()

    def __repr__(self):
        return f'{__class__.__name__}({self.first_name}, {self.last_name})'
