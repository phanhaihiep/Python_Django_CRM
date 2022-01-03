from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from customer import user_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^customer/list', views.list_customer, name='list_customer'),
    url(r'^customer/add$', views.add_customer, name='add_customer'),
    url(r'^customer/update/(?P<customer_id>[0-9]+)$', views.update_customer, name='update_customer'),
    url(r'^customer/delete/(?P<customer_id>[0-9]+)$', views.delete_customer, name='delete_customer'),
    url(r'^customer/confirm_delete/(?P<customer_id>[0-9]+)$', views.confirm_delete, name='confirm_delete'),
    url(r'^customer/search$', views.search_customer, name='search_customer'),
    url(r'^customer/validate-name$', views.validate_name, name='validate_name'),

    url(r'^register$', user_views.register_user, name='register_user'),
    url(r'^login$', user_views.login_user, name='login_user'),
    url(r'^logout$', auth_views.LogoutView.as_view(next_page="/"), name='logout_user'),

 

]