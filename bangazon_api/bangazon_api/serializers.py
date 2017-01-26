from rest_framework import serializers
from bangazon_api.models import *

class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = ("id", "name", "price", "description", "quantity", "product_category_id", "user_id",)

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ("id", "name",)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "date_of_birth")

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order 
        fields = ("id", "active", "user_id", "payment_method_id")
class ProductOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = ("id", "product_id", "order_id")

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ("id", "name", "account_number", "user_id")