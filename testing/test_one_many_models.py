import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'customer.settings')
django.setup()
os.getcwd()
from customer.models import Customer, Store, Employee

customer1=Customer.objects.get(pk=1) #pk là id của place
# tên biến thì mình đặt y chang tên class viết thường
# để biến được biến này là từ đâu

print(customer1)
store = customer1.store
print(store)
employee = store.employee_set.all()
print(employee)
