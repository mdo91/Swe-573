from django.urls import path, include
from . import views

urlpatterns = [
path('create',views.create_lesson, name='create_lesson'),
path('<int:lesson_id>/edit',views.edit, name='edit_lesson'),




]
