from django import forms
from .models import Product
from django.core.exceptions import ValidationError

class ProductForm(forms.ModelForm):
# конструктор класса ProductForm наследуется от изначальной модели c помощью подкласса Meta	
	class Meta:
		model = Product
		fields = ['product_name','product_category','product_detail','product_price','product_amount']

	def clean_product_name(self):
		new_product_name = self.cleaned_data['product_name']

		if Product.objects.filter(product_name__iexact=new_product_name).count():
			raise ValidationError('Товар с названием "{}" уже существует!'.format(new_product_name))		
		return new_product_name

# мы не описываем функцию сохранения(метод ".save()") поскольку он уже есть в ModelForm

	
