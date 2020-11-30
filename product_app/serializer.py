from rest_framework import  serializers
from product_app.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name',
        'description',
        'uuid',
        'created_at',
        'updated',
        'logo',
        'rotate_duration'
        )