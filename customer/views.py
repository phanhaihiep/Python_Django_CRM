from django.shortcuts import render
from django.shortcuts import render, redirect,HttpResponseRedirect, get_object_or_404
from django.http.response import HttpResponse, JsonResponse
from customer.forms import CustomerForm
from .models import Customer, Store, Employee
from django.core.paginator import Paginator
from django.db.models import Q
from django.conf import settings
from .models import Customer, Store, Employee
from .forms import CustomerForm
# Create your views here.
def index(request):
    customer = Customer.objects.all()
    return render(
        request=request,
        template_name='index.html', 
        context={ 
            'customer': customer,
            }
        )

def list_customer(request):
    customer = Customer.objects.all()
    paginator = Paginator(customer.order_by("id"), per_page= settings.PAGINATE_BY)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request=request,
        template_name='customer/list.html',
        context ={
            'page_obj': page_obj
        }
    )

def add_customer(request):
    form = CustomerForm()   
    if request.method == "POST":
        print(request.POST)
        form = CustomerForm(request.POST)
        if form.is_valid(): # kiểm tra, validate
            form.save()
            # redirect là chuyển về URL theo name được định nghĩa trong ulr.py
            return redirect('list_customer')
            # HttpResponseRedirect là chuyển về chính xác cái URL prefix của view
            #return HttpResponseRedirect('/place/list')
        else:
            # Form data bị lỗi
            print(form.errors)
    return render(
        request=request,
        template_name='customer/add.html',
        context={
            'form':form
        }
    )

def update_customer(request, customer_id):
    try:
        customer = Customer.objects.get(id=customer_id)
        print(customer_id)
    except Customer.DoesNotExist:
        return render(
            request=request,
            template_name='404.html',
        )
    form = CustomerForm(instance=customer)
    if request.method == "POST":
        customer.name = request.POST.get('name')
        customer.email = request.POST.get('email')
        customer.phone = request.POST.get('phone')
        customer.birthday = request.POST.get('birthday')
        customer.save()
        print(customer)
        return redirect('list_customer')
    return render(
        request=request,
        template_name='customer/update.html',
        context={
            'form':form
        }
    )

def validate_name(request):
    if request.method == "POST":
        name = request.POST['name']
        try:
            Customer.objects.get(name=name)
        except Customer.DoesNotExist:
            return JsonResponse({
                "message": f"Bạn có thể sử dụng {name}"
            }, status = 200)
    return JsonResponse({
            "message": f"{name} đã tồn tại"
        }, status= 409) # 409 conflict

def confirm_delete(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    return render(
        request=request,
        template_name='customer/confirm_delete.html',
        context={
            'customer':customer
        }
    )
def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    customer.delete() # xóa đối tượng
    return redirect('list_customer')


def search_customer(request):
    customers = []
    keyword = request.GET.get('keyword', None)
    if keyword: # kiểm tra keyword có tồn tại hay không?
        # Lấy tất cả Customer có name/phone chứa cái từ trong keyword
        customers= Customer.objects.filter(Q(name__contains=keyword) | Q(phone__contains=keyword))
    results = []
    print(results)
    for customer in customers:
        results.append({
            "id":customer.id,
            "name":customer.name,
            "email": customer.email,
            "phone":customer.phone,
            "birthday":customer.birthday,
        })
    return JsonResponse({
            "results": results
            }, status = 200)
