from rest_framework import serializers
from bangazon_api.models import *
from django.contrib.auth import models
from django.contrib.auth.models import User

class ProductCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ("id", "url", "name",)

# class ProductOrderSerializer(serializers.ModelSerializer):
#     # user = UserProfileSerializer()
#     # id = serializers.Field()
#     class Meta:
#         model = ProductOrder
#         fields = ("id", "url", "product", "order",)
#         depth = 2


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "url", "name", "price", "description", "quantity", "product_category_id", "seller",)
        depth =1

class OrderSerializer(serializers.ModelSerializer):
    # product = ProductSerializer(many= True, read_only=True)

    class Meta:
        model = Order 
        fields = ("id","url","created", "active","customer","payment_method", "product")
        depth = 1

class UserSerializer(serializers.HyperlinkedModelSerializer):

    orders = OrderSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ("id", "url", "first_name", "last_name", "username", "email", "orders")
        extra_kwargs = {"username": {"write_only": True}, "email": {"write_only": True} }
        depth = 0



class UserStaffSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User 
        fields = ('id', 'url', 'first_name', 'last_name', 'email', 'username')



class PaymentMethodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ("id", "url", "name", "account_number", "customer")

