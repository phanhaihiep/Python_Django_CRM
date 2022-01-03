from django.forms import ModelForm, Form, TextInput, Select, CheckboxInput, widgets, PasswordInput, EmailInput
from django.core.exceptions import ValidationError
from django.forms.fields import CharField, DateTimeField, EmailField
from django.contrib.auth.models import User
from .models import Customer, Store, Employee 


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__' #('name','phone')  # ('name', 'phone','email') 
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control'
            }),
             'email': EmailInput(attrs={
                'class': 'form-control'
            }),
             'phone': TextInput(attrs={
                'class': 'form-control'
            }),
            'birthday': widgets.DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'dd/mm/yyyy'
            }),
        }


class StoreForm(ModelForm):
    class Meta:
        model = Store
        fields = '__all__'
        widgets = {
            'store': Select(attrs={
                'class': 'form-control'
            }),
             'sell_products': CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
             'sell_services': CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            
        }

# Form đăng ký
class RegistrationForm(Form):
    #username, password, email, first_name, last_name
    #username không được dùng
    username = CharField(
        label="Tên đăng nhập",
        help_text="Tên dùng để đăng nhập vào website",
        max_length="50",
        widget=TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    password = CharField(
        label="Mật khẩu",
        widget=PasswordInput(
            attrs={
                'class': 'form-control'
            }

        )
    )
    # trải nghiệm người dùng
    # nếu chỉ có 1 lần nhập password thì 90% bị nhập sai
    # password và confirm password phải giống nhau
    confirm_password = CharField(
        label="Nhập lại mật khẩu",
        widget=PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    email = EmailField(
        label="Địa chỉ email",
        widget= EmailInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    first_name = CharField(
        label="Tên",
        max_length="50",
        widget=TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    last_name = CharField(
        label="Họ",
        max_length="50",
        widget=TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    def clean_username(self):
        username=self.cleaned_data['username']          
        try:
            User.objects.get(username=username) 
            raise ValidationError(f"Tên '{username}' đã tồn tại, vui lòng chọn tên khác")
        except User.DoesNotExist: 
            return username 

    def clean_confirm_password(self):
        password = self.cleaned_data['password']       
        confirm_password = self.cleaned_data['confirm_password']          
        if password != confirm_password:
            raise ValidationError(f"Mật khẩu không khớp, vui lòng nhập lại")
        return confirm_password

    def clean_email(self):
        email = self.cleaned_data['email']          
        try:
            User.objects.get(email=email) 
            raise ValidationError(f"Email '{email}' đã tồn tại, vui lòng chọn email khác")
        except User.DoesNotExist: 
            return email

# ModelForm có sẵn hàm .save()
# Form là phải tự viết
    def save_user(self):
        return User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
        )


# Form đăng nhập

class LoginForm(Form):
    username = CharField(
        label="Tên đăng nhập",
        max_length="50",
        widget=TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    password = CharField(
        label="Mật khẩu",
        widget=PasswordInput(
            attrs={
                'class': 'form-control'
            }

        )
    )