from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from smartfields import fields
from smartfields.dependencies import FileDependency
from smartfields.processors import ImageProcessor


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField('Название', max_length=100, blank=True)
    text = models.TextField('Текст', max_length=255)
    published_date = models.DateTimeField(default=timezone.now)
    likes = models.PositiveIntegerField(default=0)
    user_likes = models.ManyToManyField(User, related_name='user_like',
                                                                    blank=True)

    def like(self):
        self.likes += 1
        self.save()

    def unlike(self):
        self.likes -= 1
        self.save()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='user', blank=False,
                                unique=True, on_delete=models.CASCADE)
    first_name = models.CharField('Имя', max_length=100, blank=True)
    second_name = models.CharField('Фамилия', max_length=100, blank=True)
    middle_name = models.CharField('Отчество', max_length=100, blank=True)
    email = models.EmailField('Email', blank=True)
    phone = models.CharField('Телефон', max_length=100, blank=True)
    description = models.CharField('О себе', max_length=100, blank=True)
    avatar = fields.ImageField('Фото', dependencies=[
        FileDependency(processor=ImageProcessor(
            format='JPEG', scale={'max_width': 200, 'max_height': 240}))],
        upload_to='',  blank=True)

# Create your models here.
