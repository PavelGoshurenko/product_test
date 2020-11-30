from django.urls import path
from product_app.api import ProductCreateApi
from product_app.api import ProductApi
from product_app.api import ProductUpdateApi
from product_app.api import ProductDeleteApi
from product_app.api import ProductRetrieveApi


urlpatterns = [
    path('create', ProductCreateApi.as_view(), name='create_product'),
    path('', ProductApi.as_view(), name='get_products'),
    path('update/<str:pk>', ProductUpdateApi.as_view(), name='update_product'),
    path('delete/<str:pk>', ProductDeleteApi.as_view(), name='delete_product'),
    path('<str:pk>', ProductRetrieveApi.as_view(), name='get_single_product'),
]
