from django.db import models
from django.urls import reverse  # импортируем функцию reverse для получения url адресса


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
                            unique=True)  # unique означает уникальность

    class Meta:
        ordering = ['name']  # field для отображения
        indexes = [
            models.Index(fields=['name']),  # указываем поле для индексации
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):  # переопределили метод вывода
        return self.name

    def get_absolute_url(self):                       # метод для получения абсолютной ссылки
        return reverse('shop:product_list_by_category',  # viewname: имя шалона url указанного нами
                       args=[self.slug])                  # аргумент соответвует первому аргументу указанному в urls.py


class Product(models.Model):
    category = models.ForeignKey(Category,  # назначаем как первичный ключ к  Категории
                                 related_name='products',  # присваеваем связанное имя
                                 on_delete=models.CASCADE)  # ставим каскадный тип удаления
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='products/%Y/%m/%d',  # выбираем куда загрузить  и фрматируем загрузку
                              blank=True)  # blank=True показывает что поле не обязательно
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,  # max_digits максимальное кол цифр
                                decimal_places=2)  # decimal_places десятичные знаки
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']  # имя товара
        indexes = [
            models.Index(fields=['id', 'slug']),  # много полярный индекс
            models.Index(fields=['name']),  # индексирование по полю name
            models.Index(fields=['-created']),  # так как есть минус индексируем по убыванию created
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])                # id подгружется из базы данных
