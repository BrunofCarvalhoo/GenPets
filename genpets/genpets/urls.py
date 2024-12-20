from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('ganho/', include('ganho.urls')),
    path('faturamento/', include('faturamento.urls')),
    path('agenda/', include('appointment_calendar.urls')),
]
