#update URLConf by including URL patterns of restaurant app
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/',include('reservation.urls')),
   path('restaurant/', include('reservation.urls')),
   path('restaurant/menu/', include('reservation.urls')),
   path('auth/', include('djoser.urls')),
   path('auth/', include('djoser.urls.authtoken'))

]
