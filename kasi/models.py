from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class Stories(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    name = models.CharField(max_length=20)
    summary = models.CharField(max_length = 80, blank=False)
    published_date = models.DateTimeField()
    def __str__(self):
        return self.name
class Comment(models.Model):
    #comment = models.ForeignKey(Stories, on_delete = models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, default= None)
    comment_text = models.TextField(blank = False)

    def __str__(self):
        return self.comment_text
