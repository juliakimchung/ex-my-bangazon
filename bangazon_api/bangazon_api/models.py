from django.db import models




class Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    price = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.TextField(max_length=300, default= '')
    product_category_id = models.ForeignKey("ProductCategory", on_delete= models.CASCADE)
    quantity = models.IntegerField()
    user_id = models.ForeignKey("User", on_delete=models.CASCADE)
   

    class Meta:
        ordering = ('name',)

class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50, blank=True, default='')
    last_name = models.CharField(max_length=50, blank=True, default='')
    date_of_birth = models.DateField(default = True)
    # date_of_birth = models.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    #on-settings.py-> DATE_INPUT_FORMATS = ('%d-%m-%Y')
    
    class Meta:
        ordering = ("last_name",)

class PaymentMethod(models.Model):

    created = models.DateTimeField(auto_now_add= True)
    name = models.CharField(max_length=50, default="")
    account_number = models.CharField(max_length=100, blank = True, )
    user_id = models.ForeignKey('User', on_delete=models.CASCADE)

    class Meta:
        ordering = ("name",)



class Order(models.Model):

    active = models.BooleanField(default = False)
    user_id= models.ForeignKey("User", on_delete=models.CASCADE)
    payment_method_id = models.ForeignKey("PaymentMethod", on_delete=models.CASCADE )

    class Meta:
        ordering = ('user_id',)



class ProductOrder(models.Model):

    product_id = models.ForeignKey("Product", on_delete = models.CASCADE)
    order_id = models.ForeignKey("Order", on_delete = models.CASCADE)
    class Meta:
        ordering = ('order_id',)

class ProductCategory(models.Model):

    name = models.CharField(max_length=50, default = "")












