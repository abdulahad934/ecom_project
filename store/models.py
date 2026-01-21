from django.db import models
import datetime


# Categories of Products
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    # @daverbb
    class Meta:
        verbose_name_plural = "Categories"
    
# Customers of the E-commerce site
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Products available in the store
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, default='', blank=True, null=True)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    stock_quantity = models.PositiveIntegerField(default=0, null=True, blank=True)
    image = models.ImageField(upload_to='uploads/product', null=True, blank=True)
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(
        default=0, max_digits=10, decimal_places=2, null=True, blank=True
    )

    def __str__(self):
        return self.name



# Orders placed by Customers
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(default=datetime.datetime.now)
    address = models.CharField(max_length=200, default='', blank=True)
    phone = models.CharField(max_length=15, default='', blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id} by {self.customer.first_name}"


