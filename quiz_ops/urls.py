from django.urls import path 
from .views import * 

urlpatterns = [
   path('save-quiz/',QuizResultView.as_view()),
]
