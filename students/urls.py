from django.urls import path
from .import views

app_name = 'students'
urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('about/', views.about, name='about'),
    path('add/',views.add_student,name = 'add_student'), 
    path('update/<int:id>/', views.update_student, name='update_student_list'),
    path('delete/<int:id>/',views.delete_student,name = 'delete_student'),  
    path('register/',views.registor,name='registor'),

]