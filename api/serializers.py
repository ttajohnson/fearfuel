from rest_framework import serializers
from fearfuel import models
from django.contrib.auth import get_user_model

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Movie
        fields = (
            'id',
            'number',
            'title',
            'image',
            'overview',
            'notes',
            'watched_by',
            'watch_list',
        )

class UserSerializer(serializers.ModelSerializer):
    consumed_movies = MovieSerializer(many=True, source="consumed", read_only=True)
    watchlist_movies = MovieSerializer(many=True, source="watchlist", read_only=True)
    
    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'consumed_movies',
            'watchlist_movies',
            'consumed',
            'watchlist',
        )
