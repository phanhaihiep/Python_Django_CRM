from django.contrib import admin
from .models import Customer, Store, Employee
# Register your models here.
admin.site.register(Customer)
admin.site.register(Store)
admin.site.register(Employee)