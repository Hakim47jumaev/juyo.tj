from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'categories', 'tags')

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'author', 'created_at')
    search_fields = ('content',)
    list_filter = ('created_at', 'question')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('question', 'author', 'created_at')
    search_fields = ('content',)
    list_filter = ('created_at', 'question')

@admin.register(Feedback)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('phone_number',)
    search_fields = ('message',)
    list_filter = ('created_at', )