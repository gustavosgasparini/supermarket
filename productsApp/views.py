from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Product, ProdType
from .forms import ProductsForm

# Create your views here.
def homepage(request):
    return render(request, 'index.html')


@login_required
def prod_logout(request):
    logout(request)
    return redirect('homepage')


@login_required
def prod_list(request):
    search_term = request.GET.get('search', None)

    if search_term:
        products = Product.objects.all()
        products = products.filter(product_name__icontains=search_term)
    else:
        products = Product.objects.order_by('product_type')

    return render(request, 'products_list.html', {'products': products})


@login_required
def prod_details(request, pk):
    products = get_object_or_404(Product, pk=pk)
    return render(request, 'products_details.html', {'products': products})


@login_required
def prod_new(request):
    form = ProductsForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('prod_list')

    return render(request, 'products_form.html', {'form': form})


@login_required
def prod_update(request, pk):
    products = get_object_or_404(Product, pk=pk)
    form = ProductsForm(request.POST or None, request.FILES or None, instance=products)

    if form.is_valid():
        form.save()
        return redirect('prod_details', pk)

    return render(request, 'products_update_form.html', {'form': form})


@login_required
def prod_delete(request, pk):
    products = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        products.delete()
        return redirect('prod_list')

    return render(request, 'product_delete.html', {'products': products})