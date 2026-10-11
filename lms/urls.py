from django.urls import path
from rest_framework.routers import DefaultRouter

from lms.views import (
    CourseViewSet,
    LessonListCreateAPIView,
    LessonRetrieveUpdateDestroyAPIView,
)

app_name = 'lms'

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')

urlpatterns = [
    path('lessons/', LessonListCreateAPIView.as_view(), name='lesson_list'),
    path('lessons/<int:pk>/', LessonRetrieveUpdateDestroyAPIView.as_view(), name='lesson_detail'),
]

urlpatterns += router.urls
