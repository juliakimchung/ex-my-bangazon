from bangazon_api.models import *
from bangazon_api.serializers import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from rest_framework.reverse import reverse
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework import renderers
from rest_framework.views import APIView 
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """

    This viewset automatically provides "list", "create", "retrieve", "update", and "destroy" actions.
    This viewset will be picked up on when the UserProfileSerializer is called by get_serializer_class function is called
    """
    queryset = User.objects.all()
    def get_serializer_class(self):
        if self.request.user.is_staff:
            return UserStaffSerializer
        return UserSerializer

    


class OrderViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve', 'update', and 'destroy' actions.
    Additionally we also provide an extra 'highlight' action.

    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer 

    

class PaymentMethodViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve', 'update' and 'destroy' actions.

    Additionally we also provide an extra 'highlight' action.
    """
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer

    

class ProductViewSet(viewsets.ModelViewSet):
    """

    This viewset automatically provides 'list', 'create', 'retrieve', 'update', and 'destroy' actions.
    Additionally we also provide an extra 'highlight' action.

    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 

    


# class ProductOrderViewSet(viewsets.ModelViewSet):
#     """ 
#     This viewset automatically provides 'list', 'create', 'retreive', 'update' and 'destroy' actions.
#     Additionaly we also provide an extra 'hightlight' action.
#     """
#     queryset = ProductOrder.objects.all()
#     serializer_class = ProductOrderSerializer

    


class ProductCategoryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically porvides 'list, 'create, 'retrieve', 'update', and 'destroy' actions.
    Additionally we also provide an extra 'highlight' action.
    """

    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

    