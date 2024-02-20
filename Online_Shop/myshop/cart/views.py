from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST  # Post запросы так как карзина посылает запросы приложению
from shop.models import Product  # import Product (товара)
from .cart import Cart  # import Cart(корзины)
from .forms import CartAddProductForm  # import Form( формы корзины)
from coupons.forms import CouponApplyForm # преедставление купона в коризине
from shop.recommender import Recommender

# Create your views here.
@require_POST
def cart_add(request, product_id):
    """
    Процесс добавления в корзину
    :param request:
    :param product_id:
    :return:
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
    return redirect('cart:cart_detail') # перенаправление на url адресс cart_detail

@require_POST
def cart_remove(request, product_id):
    """
    Процес удаления из корзины
    :param request:
    :param product_id:
    :return:
    """
    card = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    card.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
                            'quantity': item['quantity'],
                            'override': True})
    coupon_apply_form = CouponApplyForm()

    r = Recommender()
    cart_products = [item['product'] for item in cart]
    if(cart_products):
        recommended_products = r.suggest_products_for(cart_products,
                                                      max_results=4)
    else:
        recommended_products = []

    return render(request,
                  'cart/detail.html',
                  {'cart': cart,
                   'coupon_apply_form': coupon_apply_form,
                   'recommended_products': recommended_products})