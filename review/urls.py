from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('review/<int:id>', views.review, name='review'),
    path('review_rate', views.review_rate, name='review_rate'),
    path('delete/<int:id>', views.delete, name="delete"),
   
]