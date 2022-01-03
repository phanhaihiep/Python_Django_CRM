import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'customer.settings')
django.setup()
from customer.models import Customer, Store, Employee
# cùng folder thì .
# khác folder thì tên file

keyword  = input("Hãy nhập từ khóa cần tìm: ")
matched_customer= Customer.objects.filter(name__contains=keyword)
matched_store= Store.objects.filter(store__name__contains=keyword)
print("Danh sách các Customers tìm được")
print("{0:>5},{1:>20},{2:>20}".format("Id", "Tên", "Email", "Số điện thoại", "Birthday"))
for customer in matched_customer:
    print("{0:>5},{1:>20},{2:>20}".format(customer.id, customer.name, customer.email, customer.phone,  customer.birthday))

print("Danh sách các Restaurants tìm được")
print("{0:>5},{1:>20},{2:>20}".format("Id", "Tên", "Địa chỉ"))
for store in matched_store:
    print("{0:>5},{1:>20},{2:>20}".format(store.customer.name, customer.name, customer.phone))
