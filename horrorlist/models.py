from django.db import models

class ConsumedMovie(models.Model):
    title = models.CharField(verbose_name="movie title", max_length=200)
    date_added = models.DateTimeField(verbose_name="date consumed", auto_now=True)
    is_consumed = models.BooleanField(verbose_name="is consumed", default=False)
    
