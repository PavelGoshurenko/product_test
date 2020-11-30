from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from product_app.serializer import ProductSerializer
from product_app.models import Product
from rest_framework.exceptions import APIException


class ChangindDenied(APIException):
    status_code = 403
    default_detail = 'You are not allowed to modify this product.'
    default_code = 'access_denied'


class ProductCreateApi(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductApi(generics.ListAPIView):
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        modified = self.request.query_params.get('modified', None)
        if modified in ['true', 'false']:
            is_modified = True if modified == 'true' else False
            return Product.objects.filter(modified=is_modified)
        return Product.objects.all()


class ProductUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def update(self, request, *args, **kwargs):
        product = self.get_object()
        if product.modified:
            raise ChangindDenied()
        product.modified = True
        product.save()
        return super().update(request, *args, **kwargs)


class ProductDeleteApi(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveApi(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
