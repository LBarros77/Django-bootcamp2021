from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.projects, name='projects_page'),
    path('create-project/', views.create_project, name='create_project'),
    path('project/<str:pk>/', views.project, name='project_page'),
    path('update-project/<str:pk>/', views.update_project, name='update_project'),
    path('delete-project/<str:pk>/', views.delete_project, name='delete_project'),
]

# urlpatterns = [
#     url(r'^projects/$', views.projects, name='projects_page'),
#     url(r'^project/<str:pk>/$', views.project, name='project_page'),
#     url(r'^create-project/$', views.create_project, name='create_project'),
#     url(r'^update-project/<str:pk>/$', views.update_project, name='update_project'),
#     url(r'^delete-project/<str:pk>/$', views.delete_project, name='delete_project'),
# ]

# urlpatterns = [
#     path('projects/', views.projects, name='projects_page'),
#     path('create-project/', views.create_project, name='create_project'),
#     re_path(r'^project/(?P<pk>[-a-z0-9]+)/$', views.project, name='project_page'),
#     re_path(r'^update-project/(?P<pk>[-a-z0-9]+)/$', views.update_project, name='update_project'),
#     re_path(r'^delete-project/(?P<pk>[-a-z0-9]+)/$', views.delete_project, name='delete_project'),
# ]