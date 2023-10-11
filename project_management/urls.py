from django.urls import path

from project_management import views


urlpatterns = [
   path('', views.index, name='home'),
   path('projects/', views.project_list, name='projects'),
   path('create_project/', views.create_project, name='create_project'),
   path('project_task/<int:pk>', views.project_task, name='project_task'),
   path('create_task/<int:pk>', views.create_task, name='create_task'),
   path('task_detail/<int:pk>', views.task_detail, name='task_detail'),
]
