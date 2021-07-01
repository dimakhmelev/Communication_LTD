from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    name = models.CharField(max_length=100)
    cost = models.IntegerField()

    def __str__(self):
        return self.title