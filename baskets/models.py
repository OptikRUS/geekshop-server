from django.db import models

from users.models import User
from products.models import Product


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('количество', default=0)
    created_timestamp = models.DateTimeField('время', auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price

    def total_quantity(self):
        baskets = Basket.objects.filter(user=self.user)
        total_quantity = 0
        for basket in baskets:
            total_quantity += basket.quantity
        return total_quantity

    def total_sum(self):
        baskets = Basket.objects.filter(user=self.user)
        total_sum = 0
        for basket in baskets:
            total_sum += basket.sum()
        return total_sum

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
