from rest_framework import generics, permissions
from .models import Category, Tag, Question, Answer, Review
from .serializer import*
from django.shortcuts import get_object_or_404
from rest_framework.filters import  SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication



class UserProfileDetail(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.userprofile

class UserProfileUpdate(generics.UpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.userprofile

class UserStatistics(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserStatisticsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user



class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']
     

class TagListCreate(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']
     

class QuestionListCreate(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['categories', 'tags']
    search_fields = ['title', 'content']
    permission_classes = [permissions.IsAuthenticated]

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionDetailSerializer
     

class AnswerListCreate(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['question', 'author']
    search_fields = ['question', 'author']
     

class AnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
     

class ReviewListCreate(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['question', 'author']
    search_fields = ['question', 'author']
     

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
     

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def vote_question(request, pk, vote_type):
    question = get_object_or_404(Question, pk=pk)
    if vote_type == 'like':
        question.likes += 1
    elif vote_type == 'dislike':
        question.dislikes += 1
    question.save()
    return Response({'status': 'vote recorded'})

@api_view(['POST'])
def vote_answer(request, pk, vote_type):
    answer = get_object_or_404(Answer, pk=pk)
    if vote_type == 'like':
        answer.likes += 1
    elif vote_type == 'dislike':
        answer.dislikes += 1
    answer.save()
    return Response({'status': 'vote recorded'})




class FeedbackListCreate(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name']
    search_fields = ['name']



class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)