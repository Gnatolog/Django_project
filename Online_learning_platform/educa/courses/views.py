from django.shortcuts import render
from django.views.generic.list import ListView # класс для получения списков
from .models import Course  # импортируем класс для которого будем
                            # реализовывать представление
from django.views.generic.edit import (
    CreateView,  # класс для создания представления
    UpdateView,  # класс для обновления представления
    DeleteView,  # класс для удаления представления
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,  # миксин для логин
    PermissionRequiredMixin  # предостовляет пользоватею доступ
                             # представлению с конкретным разрешением
)

class ManageCourseListView(ListView):
    model = Course
    template_name = 'courses/manage/course/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)


class OwnerEditMixin:
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class OwnerCourseMixin(OwnerMixin,
                       LoginRequiredMixin,
                       PermissionRequiredMixin):
    model = Course
    fields = ['subject', 'title', 'slug', 'overview']
    success_url = reverse_lazy('manage_course_list')


class OwnerCourseEditMixin(OwnerCourseMixin, OwnerEditMixin):
    template_name = 'courses/manage/course/form.html'



class ManageCourseListView(OwnerCourseMixin, ListView):
    """
    Класс который отвечает определенному функционалу при представление
    """
    template_name = 'courses/manage/course/list.html' # создаём url для данного функционала
    permission_required = 'courses.view_course'
class CourseCreateView(OwnerCourseEditMixin, CreateView):
    permission_required = 'courses.add_course'

class CourseUpdateView(OwnerCourseEditMixin, UpdateView):
    permission_required = 'courses.change_course'

class CourseDeleteView(OwnerCourseMixin, DeleteView):
    template_name = 'courses/manage/course/delete.html'
    permission_required = 'courses.delete_course'
