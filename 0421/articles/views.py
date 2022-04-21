from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_list_or_404, get_object_or_404

from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
# Create your views here.
@api_view(['GET', 'POST'])
def article_list(request):
    articles = get_list_or_404(Article)
    if request.method == 'GET':
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        # serializer = ArticleSerializer(article) 틀린 부분
        article.delete()
        data = {
            'delete': f'데이터 {article_pk}번이 삭제되었습니다.',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET'])
def comments_list(request):
    comments = get_list_or_404(Comment)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk = article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # serializer.save() 틀린 부분
        serializer.save(article = article)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk = comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        data = {
            'delete': f'코멘트 {comment_pk}번이 삭제되었습니다',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)