from django.db import models
from datetime import datetime
from myhome_dj.users.models import User

# Create your models here.
class Expenses(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=150)
    TYPE_CHOICES = [
        ('food', 'Food'),
        ('entertainment', 'Entertainment'),
        ('living', 'Living')        
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='food')
    amount = models.FloatField(max_length=10, null=False)
    details = models.TextField(max_length=256, null=True)
    date_of_expense = models.DateTimeField(default=datetime.now, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Files(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=150)
    type = models.CharField(null=True, max_length=50)
    date_of_upload = models.DateTimeField(default=datetime.now, null=False)
    contents = models.BinaryField(null=True)
    size = models.FloatField(default=0)
    expense = models.ForeignKey(Expenses, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class DjFiles(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.FileField()

    def __str__(self):
        return self.name

