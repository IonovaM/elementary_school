from django.urls import path
from . import views

urlpatterns = [
    path('', views.school_home, name='school_home'),
    path('classes/', views.class_list, name='class_list'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teacher/<int:teacher_id>/', views.teacher_dashboard, name='teacher_dashboard'),
    # path('teacher/class/<int:class_id>/add_homework/', views.add_homework, name='add_homework'),
    path('student/<int:student_id>/', views.student_dashboard, name='student_dashboard'),
    path('parent/<int:parent_id>/', views.parent_dashboard, name='parent_dashboard'),
]
