from django.urls import path
from product_app.api import ProductCreateApi, ProductApi, ProductUpdateApi, ProductDeleteApi


urlpatterns = [
    path('api/create',ProductCreateApi.as_view()),
    path('api',ProductApi.as_view()),
    path('api/update/<str:pk>',ProductUpdateApi.as_view()),
    path('api/delete/<str:pk>',ProductDeleteApi.as_view()),
]