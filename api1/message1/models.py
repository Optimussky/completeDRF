from django.db import models

# Create your models here.
class MessageModel(models.Model):
    uuid = models.CharField(max_length=150)
    username = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.username
    