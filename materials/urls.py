from django.urls import path, include
from . import views

urlpatterns = [
path('create',views.create_content, name='create_content'),
path('<int:content_id>/edit',views.edit, name='edit_content'),




]
