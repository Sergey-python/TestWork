from django.shortcuts import redirect

def redirect_products(request):
	return redirect('list_products_url', permanent=True)