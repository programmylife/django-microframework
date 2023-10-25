from django.db import models


class Post(models.Model):
    body = models.TextField()
