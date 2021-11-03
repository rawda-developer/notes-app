from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=CASCADE, related_name='notes')
    