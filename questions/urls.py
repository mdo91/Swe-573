from django.urls import path, include
from . import views

urlpatterns = [
path('create',views.create_question, name='create_question'),
path('<int:content_id>/edit',views.edit, name='edit_question'),




]
