from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView # надстройка апи над джанго drf
from rest_framework.response import Response
from courses.models import Subject, Course # класс к котрому будет доступ апи
from courses.api.serializers import SubjectSerializer, CourseSerializer  # класс api который будет работать
from rest_framework.authentication import BasicAuthentication # импортируем класс аутентийфикации
from rest_framework.permissions import IsAuthenticated # класс разрешений для пользоватлей
from rest_framework import viewsets # для создания набора представлений и маршрутизаторов
from rest_framework.decorators import action # импортируем функцию декоратор
from courses.api.permissions import IsEnrolled
from courses.api.serializers import CourseWithContentsSerializer
class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer



class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(
        detail=True,
        methods=['post'],
        authentication_classes=[BasicAuthentication],  # проверям аутентификацию
        permission_classes=[IsAuthenticated], # разрешния для авторизированых пользователей

    )
    def enroll(self, request, *args, **kwargs):
        course = self.get_object()
        course.students.add(request.user)
        return Response({'enrolled': True})


    @action(detail=True,
            methods=['get'],
            serializer_class=CourseWithContentsSerializer,
            authentication_classes=[BasicAuthentication],
            permission_classes=[IsAuthenticated, IsEnrolled])
    def contents(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
