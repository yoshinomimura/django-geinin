from django.urls import path

from . import views

app_name = 'comedians'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:comedian_id>', views.detail, name='detail'),
    path('result/<int:comedian_id>', views.result, name='result'),
]