from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'courses'         # имя приложения к которому относится api

router = routers.DefaultRouter() # обьект маршрутизатор генерирует авто url для Viewset
router.register('courses', views.CourseViewSet) # обьект Viewset



urlpatterns = [
    path('subjects/', views.SubjectListView.as_view(),
         name='subject_list'),
    path('subjects/<pk>/', views.SubjectDetailView.as_view(),
         name='subject_detail'),
    path('', include(router.urls)), # базовая страница api

]