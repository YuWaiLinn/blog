from django.urls import path, include

# apis
urlpatterns = [
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
]