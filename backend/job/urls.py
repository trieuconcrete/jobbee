from django.urls import path
from . import views

urlpatterns = [
    path('jobs', views.get_all_jobs, name='jobs.get_all_jobs'),
    path('jobs/<str:pk>/', views.get_job, name='jobs.get_job'),
    path('jobs/new/', views.new_job, name='jobs.new_job'),
    path('jobs/<str:pk>/update/', views.update_job, name='jobs.update_job'),
    path('jobs/<str:pk>/delete/', views.delete_job, name='jobs.delete_job'),
    path('stats/<str:topic>/', views.get_topic_stats, name='jobs.get_topic_stats'),
]
