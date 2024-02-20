from django.urls import path

from .import views

app_name = 'coupons'   # название приложения

urlpatterns = [
    path('apply/', views.coupon_apply, name='apply')
]