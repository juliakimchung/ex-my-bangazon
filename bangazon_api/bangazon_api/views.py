from bangazon_api.models import *
from bangazon_api.serializers import *
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework import renderers
from rest_framework.views import APIView 
from rest_framework.decorators import detail_route
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """

    This viewset automatically provides "list", "create", "retrieve", "update", and "destroy" actions.
    Additionally we also provide an extra 'highlight' action.

    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        user = self.get_object()
        return Response(user.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OrderViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve', 'update', and 'destroy' actions.
    Additionally we also provide an extra 'highlight' action.

    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer 

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        order = self.get_object()
        return Response(order.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PaymentMethodViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve', 'update' and 'destroy' actions.

    Additionally we also provide an extra 'highlight' action.
    """
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])

    def highlight(self, request, *args, **kwargs):
        # *args is for list, **kwargs is for dict
        PaymentMethod = self.get_object()
        return Response(PaymentMethod.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProductViewSet(viewsets.ModelViewSet):
    """

    This viewset automatically provides 'list', 'create', 'retrieve', 'update', and 'destroy' actions.
    Additionally we also provide an extra 'highlight' action.

    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *arg, **kwargs):
        ProductView = self.get_object()
        return Response(ProductView.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProductOrderViewSet(viewsets.ModelViewSet):
    """ 
    This viewset automatically provides 'list', 'create', 'retreive', 'update' and 'destroy' actions.
    Additionaly we also provide an extra 'hightlight' action.
    """
    queryset = Product.objects.all()
    serializer_class = ProductOrderSerializer

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])

    def highlight(self, request, *args, **kwargs):
        prodOrder= self.get_object()
        return Responses(prodOrder.highlighted)


class ProductCategoryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically porvides 'list, 'create, 'retrieve', 'update', and 'destroy' actions.
    Additionally we also provide an extra 'highlight' action.
    """

    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])

    def highlight(self, request, *args, **kwargs):
        prodOrder= self.get_object()
        return Responses(prodOrder.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)