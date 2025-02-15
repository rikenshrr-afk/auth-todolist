from django.urls import path,include
from home import views



urlpatterns = [
    path('',views.index,name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edittask/<int:task_id>', views.edit_task,name='edit_task'),
    path('deletetask/<int:task_id>', views.delete_task,name='delete_task'),
    

]

