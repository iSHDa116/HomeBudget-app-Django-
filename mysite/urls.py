from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path("", include('homebudget.urls')),
    path("admin/", admin.site.urls),
]
