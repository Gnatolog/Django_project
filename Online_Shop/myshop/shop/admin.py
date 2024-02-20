from django.contrib import admin
from .models import Category, Product    # испортируем из модуля models созданные классы

# Register your models here.
@admin.register(Category)   # Добавляем по очереди классы
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']   # поля которые будут отображатся а админке
    prepopulated_fields = {'slug': ('name',)}  # поле slug будет заполнено атоматом из поля name

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'created', 'updated'] # поля которые будут отображатся а админке
    list_filter = ['available', 'created', 'updated']  # поля которые фильтруются
    list_editable = ['price', 'available']  # поля которые можно менять в админке
    prepopulated_fields = {'slug': ('name',)} # поле slug будет заполнено атоматом из поля name


