from django import views
from django.shortcuts import render
from fearfuel.models import Movie
from rest_framework import generics, viewsets, permissions
from .serializers import MovieSerializer, UserSerializer
from django.contrib.auth import get_user_model

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class CurrentUserViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user
