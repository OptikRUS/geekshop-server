from django.db import models


class ProductCategory(models.Model):
    name = models.CharField('название категории', max_length=64, unique=True)
    description = models.TextField('описание', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория продуктов'
        verbose_name_plural = 'категории продуктов'


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField('название товара', max_length=256, unique=True)
    image = models.ImageField('изображение товара', upload_to='products_images', blank=True, null=True)
    description = models.CharField('описание', max_length=256)
    price = models.DecimalField('цена', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField('количество на складе', default=0)

    def __str__(self):
        return f'Продукт {self.name} | Категория: {self.category.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
