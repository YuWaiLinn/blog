from django.urls import path, include

# apis
apiurlpatterns = [
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
]