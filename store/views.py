from django.shortcuts import render,  get_object_or_404, redirect
from django.contrib import messages
from .models import Product
from .forms import ProductForm
from django.views.generic import ListView, DetailView, UpdateView, CreateView,DeleteView
from django.urls import reverse_lazy




# def product_list(request):
#     products = Product.objects.all()
#     return render(request, 'store/product_list.html', {'products': products})

class ProductListView(ListView):
    model = Product
    template_name = 'store/product_list.html'
    context_object_name = 'products'

# def product_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     return render(request, 'store/product_detail.html', {'product': product})

class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product_detail.html'
    context_object_name = 'product'


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'store/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        messages.success(self.request, f'Товар "{self.object.name}" успешно удален!')
        return super().form_valid(form)

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'store/product_create.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        product = form.save()
        messages.success(self.request, f'Товар "{product.name}" создан!')
        return redirect('product_detail', pk=product.pk)

# def product_create(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             product = form.save()
#             messages.success(request, f'Товар "{product.name}" успешно создан!')
#             return redirect('product_detail', pk=product.pk)
#     else:
#         form = ProductForm()
#     return render(request, 'store/product_create.html', {'form': form})



# def product_update(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     if request.method == 'POST':
#         form = ProductForm(request.POST, instance=product)
#         if form.is_valid():
#             product = form.save()
#             messages.success(request, f'Товар "{product.name}" успешно обновлен!')
#             return redirect('product_detail', pk=product.pk)
#     else:
#         form = ProductForm(instance=product)
#     return render(request, 'store/product_update.html', {'form': form, 'product': product})

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'store/product_update.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        product = form.save()
        messages.success(self.request, f'Товар "{product.name}" обновлен!')
        return redirect('product_detail', pk=product.pk)