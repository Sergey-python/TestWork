from django.db import models

class Product(models.Model):
	
	product_name = models.CharField('Название', max_length=20, unique=True)
	product_category = models.CharField('Категория', max_length=20)
	product_detail = models.CharField('Описание', max_length=200)
	product_price = models.FloatField('Цена')
	product_amount = models.SmallIntegerField('Количество')

	def __str__(self):
		return self.product_name
# формируем отсортированный список, чтобы товары одной категории находились рядом
	class Meta:
		ordering = ['product_category','product_name'] 