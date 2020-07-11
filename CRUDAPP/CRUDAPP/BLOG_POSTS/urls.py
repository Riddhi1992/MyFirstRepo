from django.urls import path
from . import views
urlpatterns = [
    path('crud/', views.StudentsView.as_view()),
    path('crud/<int:pk>', views.StudentsView.as_view()),
]
