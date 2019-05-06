from django.urls import path, include
from . import views

urlpatterns = [
path('create',views.create, name='create'),
path('<int:topic_id>/edit',views.edit, name='edit'),




]
