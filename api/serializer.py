from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ['user', 'bio']

class UserProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['bio']

class UserStatisticsSerializer(serializers.ModelSerializer):
    questions_count = serializers.SerializerMethodField()
    answers_count = serializers.SerializerMethodField()
    votes_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'questions_count', 'answers_count', 'votes_count']

    def get_questions_count(self, obj):
        return Question.objects.filter(user=obj).count()

    def get_answers_count(self, obj):
        return Answer.objects.filter(user=obj).count()

    def get_votes_count(self, obj):
        return obj.question_set.aggregate(votes_count=models.Sum('likes'))['votes_count'] or 0







class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

    def get_queryset(self):
        queryset = super().get_queryset()
        keyword = self.request.query_params.get('keyword', None)
        category = self.request.query_params.get('category', None)
        tag = self.request.query_params.get('tag', None)

        if keyword:
            queryset = queryset.filter(content__icontains=keyword)
        if category:
            queryset = queryset.filter(categories__name=category)
        if tag:
            queryset = queryset.filter(tags__name=tag)

        return queryset

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
    
class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class QuestionDetailSerializer(serializers.ModelSerializer):
    answer=AnswerSerializer(many=True,read_only=True)

    class Meta:
        model = Question
        fields = ['title','content','author','categories','tags','created_at','answer']

