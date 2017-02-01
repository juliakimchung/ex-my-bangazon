from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    """
    Class to represent a product for sale on Bangazon
    tied to a
    particular User(customer) of bangazon API
    Extension of models.Model

    Variables:
        created: the current local date and time of creation
        name: the product's name
        
        user: the foreign key of the user, related_name is for the PaymentMethod model: related_name should be lowercase, pluralized model name

    """
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    price = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.TextField(max_length=300, default= '')
    product_category = models.ForeignKey("ProductCategory", related_name= "products", on_delete= models.CASCADE)
    quantity = models.IntegerField()
    seller = models.ForeignKey(User, related_name="products", on_delete=models.CASCADE)

    def __str__(self):
        """
        Method to create a string representing a Product sold by a
        particular User(seller) of Bangazon API
        """
        return self.name
   

    class Meta:
        ordering = ('name',)


class PaymentMethod(models.Model):

    """
    This is a class to represent a payment method to a user of  bangazon api
    Variables:
        created: the current local date and time of creation
        name: the payment method's name
        account_number: the payment method's unique identifier
        user: the foreign key of the user, related_name is for the PaymentMethod model: related_name should be lowercase, pluralized model name
    """

    created = models.DateTimeField(auto_now_add= True,)
    name = models.CharField(max_length=50, default="")
    account_number = models.CharField(max_length=100, blank = True, default="" )
    customer = models.ForeignKey(User, related_name="payment_methods",  on_delete=models.CASCADE)

    def __str__(self):
    
        return self.name
        
    class Meta:
        """
        Class defining metadata for results of querying the Payment Method
        table of Bangazon API
        """
        ordering = ("name",)
        



class Order(models.Model):
    """
    Class to create a table representing an Order, tied to a
    particular User(customer) of bangazon API
    Extension of models.Model

    Variables:
        active: A boolean denoting whether the order is being processed
        created: the current local date and time of creation
        payment_method_id: the foreign key of the user's payment method, only
            needed when the order is "active", related_name is for the Order model: related_name should be lowercase, pluralized model name

        user: the foreign key of the User(customer)related_name is for the Order model: related_name should be lowercase, pluralized model name
    """

    active = models.BooleanField(default = True)
    created = models.DateTimeField(auto_now_add=True)

    customer= models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE)
    payment_method = models.ForeignKey("PaymentMethod", related_name="orders", on_delete=models.CASCADE )
    product = models.ManyToManyField(Product)
   
    def __str__(self):  
        return str(self.id)
        """
        Method to create a string representing a Order of a particular User
        (customer) of Bangazon API
        """
    class Meta:
        ordering = ('customer',)



# class ProductOrder(models.Model):

#     """
#     This class is to represent Product order on  Bangazon
#     Class to create a table representing a Product Order, tying products to a
#     particular Order
#     Extension of models.Model

#     Variables:
#         product: foreign key of an added product, related_name is for the ProductOrder model: related_name should be lowercase, pluralized model name

#         order: foreign key of the order, related_name is for the ProductOrder model: related_name should be lowercase, pluralized model name

#     """

#     product = models.ForeignKey("Product", related_name="product_orders", on_delete = models.CASCADE)
#     order = models.ForeignKey("Order", related_name="product_orders", on_delete = models.CASCADE)

#     def __str__(self):
#         return str(self.id)

#     class Meta:
#         ordering = ('order',)

class ProductCategory(models.Model):

    """ 
    This class is to represent a category of products on Bangazon
    Extension of models.Model

    Variables:
        name: the Product Category's name
    """
    name = models.CharField(max_length=50, default = "")

    def __str__(self):
        return self.name
    """
    Method to create a string representing a Product Category of
    Bangazon API
    """
    class Meta:
    
        ordering = ('name',)


















