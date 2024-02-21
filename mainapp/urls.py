from django.urls import path

from mainapp.apps import MainappConfig
from mainapp.views import index, CategoryListView, ProductListView

app_name = MainappConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('<int:pk>/mainapp/', ProductListView.as_view(), name='product_list'),
]
