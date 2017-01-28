from django.db import models



class Product(models.Model):
    """
    Class to represent a product for sale on Bangazon

    """
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    price = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.TextField(max_length=300, default= '')
    product_category_id = models.ForeignKey("ProductCategory", on_delete= models.CASCADE)
    quantity = models.IntegerField()
    user_id = models.ForeignKey("UserProfile", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
   

    class Meta:
        ordering = ('name',)

class UserProfile(models.Model):

    """
    This is a class to represent a user on Bangazon
    """
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50, blank=True, default='')
    last_name = models.CharField(max_length=50, blank=True, default='')
    date_of_birth = models.DateField(default = True)
    # date_of_birth = models.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    #on-settings.py-> DATE_INPUT_FORMATS = ('%d-%m-%Y')

    def __str__(self):
        return self.first_name + " " + self.last_name
    
    class Meta:
        ordering = ("last_name",)

class PaymentMethod(models.Model):

    """
    This is a class to represent a payment method to a user on Bangazon

    """

    created = models.DateTimeField(auto_now_add= True)
    name = models.CharField(max_length=50, default="")
    account_number = models.CharField(max_length=100, blank = True, )
    user_id = models.ForeignKey('UserProfile', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
        



class Order(models.Model):

    active = models.BooleanField(default = False)
    user_id= models.ForeignKey("UserProfile", on_delete=models.CASCADE)
    payment_method_id = models.ForeignKey("PaymentMethod", on_delete=models.CASCADE )

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('user_id',)



class ProductOrder(models.Model):

    """
    This class is to represent Product order on  Bangazon

    """

    product_id = models.ForeignKey("Product", on_delete = models.CASCADE)
    order_id = models.ForeignKey("Order", on_delete = models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('order_id',)

class ProductCategory(models.Model):

    """ 
    This class is to represent a category of products on Bangazon
    """
    name = models.CharField(max_length=50, default = "")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


















