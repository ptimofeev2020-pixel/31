from django.urls import path
from rest_framework.routers import DefaultRouter

from users.views import UserViewSet, PaymentListAPIView

app_name = 'users'

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('payments/', PaymentListAPIView.as_view(), name='payment_list'),
]

urlpatterns += router.urls
