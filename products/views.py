from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import View
from .models import Product
from .forms import ProductForm
from django.core.paginator import Paginator

from django.contrib.auth.mixins import LoginRequiredMixin # ограничеваем доступ к добавлению, редактированию и удалению

# список всех товаров
def list_products(request):
	products = Product.objects.all()
	row_names = ['Название','Категория','Описание','Цена, руб/кг','Количество, кг']
	# постраничная навигация, сделал только для главной страницы
	paginator = Paginator(products, 10)
	page_number = request.GET.get('page',1)
	page = paginator.get_page(page_number)
	return render(request, 'products/index.html', context={'page_object': page,'row_names': row_names})

# список всех категорий
def list_categories(request):
	categories = []
	for product in Product.objects.all():
		categories.append(product.product_category)
	return render(request, 'products/categories.html', context = {'categories':set(categories)})

# список товаров выбранной категории
def list_products_in_category(request, product_category):
	products_in_category = Product.objects.filter(product_category = product_category)
	row_names = ['Название','Описание','Цена, руб/кг','Количество, кг']
	return render(request, 'products/products_in_category.html',
	context = {'products_in_category': products_in_category, 'product_category': product_category, 'row_names': row_names})

# форма добавления нового товара
class CreatProduct(LoginRequiredMixin,View):
	login_url = '/admin/'
	def get(self, request):
		form = ProductForm()
		return render(request, 'products/form_create_product.html', context = {'form':form})

	def post(self, request):
		bound_form = ProductForm(request.POST)
		if bound_form.is_valid():
			new_product = bound_form.save()
		return render(request, 'products/form_create_product.html', context = {'form':bound_form})

# форма редактирование товара
class EditProduct(LoginRequiredMixin,View):
	login_url = '/admin/'
	def get(self, request, product_name):
		products = Product.objects.all()
		selected_product = Product.objects.get(product_name__iexact=product_name)
		bound_form = ProductForm(instance=selected_product)	
		return render(request, 'products/form_edit_product.html',
		context={'products': products, 'bound_form': bound_form, 'product_name': product_name})

	def post(self, request, product_name):
		products = Product.objects.all()
		selected_product = Product.objects.get(product_name__iexact=product_name)
		bound_form = ProductForm(request.POST, instance=selected_product)
		if bound_form.is_valid():
			new_product = bound_form.save()
		return render(request, 'products/form_edit_product.html',
		context={'products': products, 'bound_form': bound_form, 'product_name': product_name})

# форма удаление товара
class DeleteProduct(LoginRequiredMixin,View):
	login_url = '/admin/'
	def get(self, request, product_name):
		products = Product.objects.all()
		row_names = ['Название','Категория','Описание','Цена, руб/кг','Количество, кг']			
		return render(request, 'products/form_delete_product.html',
		context={'products': products, 'row_names': row_names, 'product_name': product_name})

	def post(self, request, product_name):
		deleting_product = Product.objects.get(product_name__iexact=product_name)
		deleting_product.delete()
		return redirect(reverse('list_products_url')) # после удаления товара переходим ко всем товарам

# сортировка
def sorting(request):
	pass