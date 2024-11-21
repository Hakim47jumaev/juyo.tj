from rest_framework import serializers
from .models import *



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

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


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    question=QuestionSerializer(many=True,read_only=True)

    class Meta:
        model = UserProfile
        fields = ['user', 'bio','question']

class UserProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['bio']
 





class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'



class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

 
    
class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class QuestionDetailSerializer(serializers.ModelSerializer):
    answer=AnswerSerializer(many=True,read_only=True)

    class Meta:
        model = Question
        fields = ['title','content','author','categories','tags','created_at','answer' ]

