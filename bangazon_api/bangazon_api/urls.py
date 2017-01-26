# from django.conf.urls import url
# from . import views

# from rest_framework.urlpatterns import format_suffix_patterns

# urlpatterns = [
#     url(r'^bangazon/product/$', views.ProductList.as_view()),
#     url(r'^bangazon/(?P<pk>[0-9]+)/$', views.ProductDetail.as_view()),
#     url(r'^bangazon/order/$', views.OrderList.as_view()),
#     url(r'^bangazon/(?P<pk>[0-9]+)/$', views.OrderDetail.as_view()),
#     url(r'^bangazon/user/$', views.UserList.as_view()),
#     url(r'^bangazon/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
#     url(r'^bangazon/Product-Order/$', views.ProductOrderList.as_view()),
#     url(r'^bangazon/(?P<pk>[0-9]+)/$', views.ProductOrderDetail.as_view()),
#     url(r'^bangazon/PaymentMethod/$', views.PaymentMethodList.as_view()),
#     url(r'^bangazon/(?P<pk>[0-9]+)/$', views.PaymentMethodDetail.as_view()),

#     # url(r'^bangazon_api/(?P<slug>[\w-]+)/$','bangazon_api.views.product_order_detail' name = "product_order_detail")
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)