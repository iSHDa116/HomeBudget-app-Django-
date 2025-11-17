from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.CreateDataView.as_view(), name='create'),
    path('history', views.ListHomeView.as_view(),name="history"),
    path('delete/<int:pk>', views.DeleteDate, name='delete'),
    path('update/<int:pk>', views.UpdateDataView.as_view(),name="update"),
]