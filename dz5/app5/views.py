from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Product, Category
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm, CategoryForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_create.html'
    success_url = reverse_lazy('product_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_create.html'
    success_url = reverse_lazy('product_list')


def product_list(request):
    products = Product.objects.all()
    paginator = Paginator(products, 10)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'product_list.html', {'products': products})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_create.html', {'form': form})


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_create.html', {'form': form})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_delete.html', {'product': product})