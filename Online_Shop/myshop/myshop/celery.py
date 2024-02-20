import os
from celery import Celery  # Импортируем класс Celery

# Задаём стандартный модуль настроек Django для программы 'celery'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')
app = Celery('myshop')
app.config_from_object('django.conf:settings', namespace='CELERY')  # загружается
# конкретно прикладная конфигурация из настроек
app.autodiscover_tasks()  # авто поиск асинхронных заданий в файлк task.py каждого приложения
# зарегесрированного в INSTALLED_APPS
