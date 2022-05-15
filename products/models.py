from django.db import models


class ProductCategory(models.Model):
    name = models.CharField('название категории', max_length=64, unique=True)
    description = models.TextField('описание', blank=True, null=True)
    is_active = models.BooleanField('активность', default=True)

    class Meta:
        verbose_name = 'категория продуктов'
        verbose_name_plural = 'категории продуктов'

    def __str__(self):
        return self.name

    def safe_delete(self):
        self.is_active = False
        self.save()


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='категория')
    name = models.CharField('наименование товара', max_length=256, unique=True)
    image = models.ImageField('изображение товара', upload_to='products_images', blank=True, null=True)
    description = models.CharField('описание', max_length=256)
    price = models.DecimalField('цена за штуку', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField('количество на складе', default=0)
    is_active = models.BooleanField('активность', default=True)

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def __str__(self):
        return self.name

    def safe_delete(self):
        self.is_active = False
        self.save()
