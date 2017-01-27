from rest_framework import serializers
from bangazon_api.models import *

class ProductSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Product
    fields = ("id", "url", "name", "price", "description", "quantity", "product_category_id", "user_id",)

class ProductCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ("id", "url", "name",)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("id", "url", "first_name", "last_name", "date_of_birth")

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order 
        fields = ("id","url", "active", "user_id", "payment_method_id")
class ProductOrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductOrder
        fields = ("id", "url", "product_id", "order_id")

class PaymentMethodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ("id", "url", "name", "account_number", "user_id")