from django.shortcuts import render, get_object_or_404  # добавляем обработку ошибки get_object_or_404
from .models import Category, Product  # импортируем классы из модуля
from cart.forms import CartAddProductForm # импортируем добавление в корзину
from .recommender import Recommender   # импорируем класс рекомендаций


# Create your views here.
def product_list(request, category_slug=None):
    """

    :param request: запрос от пользователя
    :param category_slug: к какой категории обращаемся в базе данных
    :return: Возвращает html страницу с заполненными полями
    """
    category = None  # выбранная категория
    categories = Category.objects.all()  # получаем список всех категорий
    products = Product.objects.filter(available=True)  # получаем список всех товаров в наличие
    if category_slug:  # проверяем есть ли заданный каталог
        category = get_object_or_404(Category,  # если нет ошибки то Вызваем класс и присваем полю slug
                                     # значение которое ищет клиент
                                     slug=category_slug)
        products = products.filter(category=category)  # филтруем тоар по категории
    return render(request,  # возвращаем найденный результат по запросу
                  'shop/product/list.html',  # указываем щаблон html страницы приложения
                  {'category': category,  # указываем поля которые будут отображатся
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    """
    :param request: запрос по товару
    :param id:     идетификационный номер товара
    :param slug:   ппримечание товара
    :return:       Html страницу с товаром
    """
    product = get_object_or_404(
        Product,
        id=id,
        slug=slug,
        available=True)

    cart_product_form = CartAddProductForm()
    r = Recommender()
    recommended_products = r.suggest_products_for([product], 4)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form,
                   'recommended_products': recommended_products})
