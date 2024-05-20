from django.urls import path

from . import views
urlpatterns = [
   path('', views.index, name='index'),
   path('aboutme/', views.aboutme, name='aboutme'),
   path('complete/<int:id>', views.complete, name='complete'),
]
