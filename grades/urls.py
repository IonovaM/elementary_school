from django.urls import path
from . import views

urlpatterns = [
    # Добавьте маршруты по мере необходимости
    path('', views.index, name='grades_index'),  # Пример маршрута
]
