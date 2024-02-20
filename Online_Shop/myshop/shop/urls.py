from django.urls import path                    # импортируем библиотеку urls
from . import views                             # из этого же каталога ипортируем созданное
                                                # представлние обьектов на html странице

app_name = 'shop'  # создаём переменную присваеваем имя нашего приложения

# у path первый аргумент вид шаблона как будет отображатся, второй аргумент источник информации,
# третий аргумент имя шаблона по которому можно бдует к нему обращатся

urlpatterns = [                           # создаём шаблоны url адрессов для наших класс
    path('', views.product_list, name='product_list'),  # первый шаблон для списка без параметров
    path('<slug:category_slug>/', views.product_list,   # второй шаблон для списка с параметрами
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail')
]
