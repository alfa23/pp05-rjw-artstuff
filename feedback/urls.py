from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_feedback, name='view_feedback'),
    path('add/<int:product_id>/', views.add_feedback, name='add_feedback'),
    path('edit/<int:feedback_id>/', views.edit_feedback, name='edit_feedback'),
    path(
        'delete/<int:feedback_id>/',
        views.delete_feedback, name='delete_feedback'
    ),
]
