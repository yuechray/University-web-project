from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    date_published = models.DateTimeField(default=timezone.now, verbose_name="Дата публикации")
    image = models.ImageField(upload_to="media/Images/", verbose_name="Изображение", null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/detail/{self.pk}/"

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name="Новость")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", null=True, blank=True)
    text = models.TextField(verbose_name="Содержание")
    date_published = models.DateTimeField(default=timezone.now, verbose_name="Дата публикации")

    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", null=True, blank=True)
    text = models.TextField(verbose_name="Содержание")
    image = models.ImageField(upload_to="media/Images/", verbose_name="Изображение", null=True, blank=True)
    date_published = models.DateTimeField(default=timezone.now, verbose_name="Дата публикации")

    def __str__(self):
        return str(self.text)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
