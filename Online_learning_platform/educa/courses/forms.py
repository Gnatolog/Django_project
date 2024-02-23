from django import forms
from django.forms.models import inlineformset_factory  # набор форм а не одна диниамическ
                                                       # для этого указываем первый класс родитель
                                                       # второй класс дочерний и за счет этого формы будут связанны
from .models import Course, Module

ModuleFormSet = inlineformset_factory(Course,
                                      Module,
                                      fields=['title',           # поля для формы
                                              'description'],
                                      extra=2,                   # устанавливае число доп форм
                                      can_delete=True            # устанавливаем True для каждой формы
                                      )

