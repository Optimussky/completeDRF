from django.db import models


"""
class DataSystemModel(models.Model):
    uuid = models.CharField(max_length=150)
    system = models.CharField(max_length=150)
    user = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.user
"""

# Create your models here.
class MessageModel(models.Model):

    uuid = models.CharField(max_length=150)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    # key_uuid = models.ForeignKey(DataSystemModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.username


    

