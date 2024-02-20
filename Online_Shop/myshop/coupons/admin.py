from django.contrib import admin
from .models import Coupon


# Register your models here.

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'valid_from', 'valid_to',   # что будет отображатся в админке
                    'discount', 'active']
    list_filter = ['active', 'valid_from', 'valid_to']   # что фильтруем

    search_fields = ['code']   # поле по которму бкдем искать купон
