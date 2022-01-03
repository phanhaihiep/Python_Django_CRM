from django import template
from django.conf import settings
register=template.Library() # tạo biến để xác định các hàm python filter

@register.filter
def luy_thua(co_so, so_mu):
    return co_so**so_mu

#luy_thua(2,3) bình thường
# trong django template thì 2|luy_thua:3

@register.filter
def make_range(number):
    return range(1,number + 1)

@register.filter
def make_index_pagination(current_page,index):
    # current page = 3
    # indext = 1
    # index-page= 11 = pagenate_by * (current_page-1) + index
    return settings.PAGINATE_BY * (current_page -1) + index
