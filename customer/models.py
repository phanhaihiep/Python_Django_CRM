from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(verbose_name="Your name", max_length=50)
    email = models.CharField(verbose_name="Your email", max_length=50)
    phone = models.CharField(verbose_name="Phone", max_length=13)
    birthday = models.CharField(verbose_name="Your birthday", max_length=100)

    def __str__(self):
        return f"{self.name} customer"

    class Meta:
        db_table = "Customer"


class Store(models.Model):
    name = models.CharField(verbose_name="Shop's name", max_length=50)
    phone = models.CharField(verbose_name="Shop's phone", max_length=13)
    address = models.CharField(verbose_name="Shop's address", max_length=50)
    sell_service = models.BooleanField(verbose_name="Sell services", default=False)
    sell_product = models.BooleanField(verbose_name="Sell products", default=False)

    def __str__(self):
        return f"{self.store.name} the store"
    
    class Meta:
        db_table = "Store"


class Employee(models.Model):
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.name} is a employee at {self.store}"

    class Meta:
        db_table = "Employee"
