from django.db import models

from django.contrib.auth import get_user_model

class Movie(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=500)
    image = models.URLField()
    overview = models.TextField()
    notes = models.TextField()
    watched_by = models.ManyToManyField(get_user_model(), related_name="consumed", blank=True)
    watch_list = models.ManyToManyField(get_user_model(), related_name="watchlist", blank=True)