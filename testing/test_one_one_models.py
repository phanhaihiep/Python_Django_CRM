import os
import sys
import django
# python manage.py makemigration myapp
# python manage.py migrate
# python manage.py shell

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'customer.settings')
django.setup()
os.getcwd()

from customer.models import Customer, Store, Employee
print(Customer.objects.all())
