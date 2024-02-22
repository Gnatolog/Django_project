from django.urls import path  # import model for url templates
from . import views  # импортируем все классы

urlpatterns = [
    path('mine/', views.ManageCourseListView.as_view(),
         name='manage_course_list'),
    path('create/', views.CourseCreateView.as_view(),
         name='course_create'),
    path('<pk>/edit/', views.CourseUpdateView.as_view(),
         name='course_edit'),
    path('<pk>/delete/',
         views.CourseDeleteView.as_view(),
         name='course_delete'),
]