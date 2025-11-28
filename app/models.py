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


class Product(models.Model):
    name = models.CharField('Название', max_length=200)
    description = models.TextField('Описание', blank=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    manufacturer = models.CharField('Производитель', max_length=100, blank=True)
    image = models.ImageField(upload_to="media/Images/products/", verbose_name="Изображение", null=True, blank=True)
    date_added = models.DateTimeField(default=timezone.now, verbose_name="Дата добавления")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/product/{self.pk}/"

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.PositiveIntegerField('Количество', default=1)
    date_added = models.DateTimeField(default=timezone.now, verbose_name="Дата добавления")

    def __str__(self):
        return f"{self.user.username} - {self.product.name} x{self.quantity}"

    def get_total_price(self):
        return self.product.price * self.quantity

    class Meta:
        verbose_name = "Элемент корзины"
        verbose_name_plural = "Элементы корзины"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    items = models.ManyToManyField(CartItem, verbose_name="Товары")
    total_price = models.DecimalField('Общая стоимость', max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")
    is_paid = models.BooleanField('Оплачен', default=False)

    def __str__(self):
        return f"Заказ #{self.id} от {self.user.username}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"