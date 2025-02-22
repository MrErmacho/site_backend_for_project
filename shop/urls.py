from django.urls import path
from.views import catalog, orders, orders_create, product_detail

app_name = 'shop'

urlpatterns = [
    path('', catalog, name='catalog'),
    path("product/<int:product_id>/", product_detail, name="product_detail"),
    path('orders/', orders, name='orders'),
    path('orders_create/<int:product_id>/', orders_create, name='orders_create'),
]

