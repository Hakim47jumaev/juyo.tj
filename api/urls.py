from django.urls import path
from .views import *



urlpatterns = [
    path('', Home.as_view()),

    path('profile/',UserProfileDetail.as_view(),name='profile'),
    path('profile/edit',UserProfileUpdate.as_view(),name='profile-edit'),
    
     
    path('categories/', CategoryListCreate.as_view(), name='category-list-create'),
    path('tags/', TagListCreate.as_view(), name='tag-list-create'),
    path('questions/', QuestionListCreate.as_view(), name='question-list-create'),
    path('questions/<int:pk>/', QuestionDetail.as_view(), name='question-detail'),
    path('answers/', AnswerListCreate.as_view(), name='answer-list-create'),
    path('answers/<int:pk>/', AnswerDetail.as_view(), name='answer-detail'),
     

    path('questions/<int:pk>/vote/<str:vote_type>/', vote_question, name='vote-question'),
    path('answers/<int:pk>/vote/<str:vote_type>/', vote_answer, name='vote-answer'),

    path('feedback/', FeedbackListCreate.as_view(), name='feedback-list-create'),
]