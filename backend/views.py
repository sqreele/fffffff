from itertools import permutations
from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from datetime import date
from xmlrpc.client import ResponseError
from django.shortcuts import render,HttpResponse
from .permisstions import IsAuthor

from .models import Article
from .serializers import ArticleSerializers
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404



class ArticleList(APIView):
    
    permission_classes = [IsAuthor]  
    
    authentication_classes = (TokenAuthentication,SessionAuthentication)  
    
    def get(self,request):
        article = Article.objects.all()
        serializer = ArticleSerializers(article,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = ArticleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ArticleDetails(APIView):
    def get_object(self,slug):
        try:
            return Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404
        
    def get(self,request,slug):
        article = self.get_object(slug) 
        serializer = ArticleSerializers(article)
        return Response(serializer.data) 
    
    def put(self,request,slug):
        article = self.get_object(slug)
        serializer =ArticleSerializers(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  
    
    def delete(self,request,slug):
        article = self.get_object(slug) 
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
    
    
     
        




'''
@api_view(['GET','POST'])
def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializers(articles,many = True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer= ArticleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])    
def article_details(request,slug):
    try:
        article = Article.objects.get(slug=slug)
    except Article.DoesNotExist():
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serailizer = ArticleSerializers(article)
        return Response(serailizer.data) 
    elif request.method == "PUT":
        serailizer= ArticleSerializers(article,data=request.data)
        if serailizer.is_valid():
            serailizer.save()
            return Response(serailizer.data)
        return Response(serailizer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            
  '''            
    
    
'''
@csrf_exempt
def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializers(articles,many=True)
        return JsonResponse(serializer.data,safe=False)
    
    elif request.method =="POST":
        data = JSONParser().parse(request) 
        serializer = ArticleSerializers(data=data) 
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status = 201)
        return JsonResponse(serializer.errors,status =400)  
@csrf_exempt
def article_details(request,slug):
   
    try:
        article = Article.objects.get(slug=slug)
    except Article.DoesNotExist:
        return HttpResponse(status = 404)
    
    
    
    if request.method == "GET":
        serializer = ArticleSerializers(article)
        return JsonResponse(serializer.data) 
    
    elif request.method =="PUT":
        data = JSONParser().parse(request)
        serializer = ArticleSerializers(article,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status = 200)
        return JsonResponse(serializer.errors,status = 400)
    
    elif request.method == "DELETE":
         article.delete()
         return JsonResponse(status = 204)   
# Create your views here.
'''
