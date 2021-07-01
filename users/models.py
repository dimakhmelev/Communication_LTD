from django.db import models
from django.contrib.auth.models import User

DATA_PLAN_CHOICES =(
    ("1", "Ultimate  100$/m"),
    ("2", "Regular 50$/m"),
    ("3", "Free 0$/m"),
    )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    phone = models.CharField(max_length=11, default='0521111111')
    data_plan = models.CharField(default='Ultimate  100$/m', max_length=60, choices = DATA_PLAN_CHOICES)

    def __str__(self):
        return f'{self.user.username} Profile'


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100, null=True)
    Email = models.EmailField(max_length=100, null=True)
    Phone = models.CharField(max_length=11, null=True)

    def __str__(self):
        return f'{self.Name} Customer'
