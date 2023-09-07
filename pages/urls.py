from django.urls import path
from . import views



urlpatterns = [


path('' , views.index , name='index'),
path('all_blogs/' , views.all_blogs , name='all_blogs'),
path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
path('project/<int:project_id>/', views.project_detail, name='project_detail'),















]