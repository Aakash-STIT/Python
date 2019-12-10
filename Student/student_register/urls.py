from django.urls import path
from . import views

urlpatterns = [

    path('<int:id>/', views.student_form, name='student_update'),
    path('list/', views.student_list, name='student_list'),
    path('delete/<int:id>/', views.delete_student, name='student_delete')
]
