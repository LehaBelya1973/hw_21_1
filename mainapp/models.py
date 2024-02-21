from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Категория')
    description = models.TextField(verbose_name='Описание категории', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(max_length=100, verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='product_list/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за единицу')
    date_of_production = models.DateField(auto_now_add=True, verbose_name='Дата внесения товара', **NULLABLE)
    date_last_changes = models.DateField(auto_now=True, verbose_name='Дата последнего изменения', **NULLABLE)

    def __str__(self):
        return f'{self.name} {self.price} {self.category}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('name', 'price')

