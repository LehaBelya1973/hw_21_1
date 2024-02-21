from django.shortcuts import render
from django.views.generic import ListView

from mainapp.models import Product, Category


# class ProductListView(ListView):
#     model = Product
#     extra_context = {'title': 'Магазин - Главная'}
#     paginate_by = 3


def index(request):
    context = {
        'object_list': Product.objects.all()[:3],
        'category_list': Category.objects.all(),
        'title': 'Магазин - Главная',
    }
    return render(request, 'mainapp/index.html', context)


class CategoryListView(ListView):
    model = Category
    extra_context = {'title': 'Категории наших товаров:'}


# def categories(request):
#     context = {
#         'object_list': Category.objects.all(),
#         'title': 'Категории наших товаров:',
#     }
#     return render(request, 'mainapp/category_list.html', context)

class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args,**kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['title'] = f'Товары из категории {category_item.name}'

        return context_data



# def category_product(request, pk):
#     category_item = Category.objects.get(pk=pk)
#     context = {
#         'object_list': Product.objects.filter(category_id=pk),
#         'title': f'Товары из категории {category_item.name}',
#     }
#     return render(request, 'mainapp/product_list.html', context)
