from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,PermissionsMixin
# Create your models here.

class Trains(models.Model):
    categories = (
        ('Normal','Normal'),
        ('Express','Express')
    )
    id = models.AutoField(primary_key=True)
    source = models.CharField(max_length = 30,)
    destination = models.CharField(max_length = 30)
    seats_total = models.IntegerField()
    seats_res = models.IntegerField()
    types = models.CharField(choices=categories,max_length=20)
    cost = models.IntegerField()
    date = models.DateField()
    def __str__(self):
        return str(self.id)


class Users(AbstractUser):
    username = models.CharField(primary_key = True,max_length=20)
    email = models.EmailField(null=True)
    first_name = models.CharField(null=True,max_length = 20)
    last_name = models.CharField(null=True,max_length = 20)
    balance = models.IntegerField(default = 0)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = "username"
    def __str__(self):
        return self.username
 
class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    num_booked = models.IntegerField()
    users = models.ForeignKey(Users,null=True,on_delete = models.CASCADE)
    trains = models.ForeignKey(Trains,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)

