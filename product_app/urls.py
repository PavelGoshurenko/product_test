from django.urls import path
from product_app.api import ProductCreateApi, ProductApi, ProductUpdateApi, ProductDeleteApi, ProductRetrieveApi


urlpatterns = [
    path('create',ProductCreateApi.as_view()),
    path('',ProductApi.as_view()),
    path('update/<str:pk>', ProductUpdateApi.as_view()),
    path('delete/<str:pk>', ProductDeleteApi.as_view()),
    path('<str:pk>', ProductRetrieveApi.as_view()),
]