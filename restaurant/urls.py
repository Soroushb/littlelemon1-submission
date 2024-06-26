from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('menu-items/', views.MenuItemView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/', include(router.urls)),
    path('message/', views.msg),
    path('api-token-auth/', obtain_auth_token)


]
