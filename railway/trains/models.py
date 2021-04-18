from django.db import models

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
    date = models.CharField(max_length = 20)
    def __str__(self):
        return str(self.id)

class Users(models.Model):
    uid = models.CharField(primary_key = True,max_length=20)
    email = models.EmailField(null=True)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20,null=True)
    balance = models.IntegerField(default = 0)
    USERNAME_FIELD = "uid"

    def __str__(self):
        return self.uid
 
class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    num_booked = models.IntegerField()
    users = models.ForeignKey(Users,null=True,on_delete = models.SET_NULL)
    trains = models.ForeignKey(Trains,null=True,on_delete=models.SET_NULL)
    def __str__(self):
        return str(self.id)

