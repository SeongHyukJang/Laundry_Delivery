from django.db import models

class Laundry(models.Model):
    '''
ID(primary key)
Name
Latitude
Longitude
Address
    '''
    Name = models.CharField(max_length=30)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Address = models.CharField(max_length=100)

    def __str__(self):
        return self.Name

class Repair(models.Model):
    Name = models.CharField(max_length=30)
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Address = models.CharField(max_length=100)

    def __str__(self):
        return self.Name

class Customer(models.Model):

    Name = models.CharField(max_length=30)
    ID = models.CharField(max_length = 20, primary_key=True,null=False,blank=False)
    PW = models.CharField(max_length = 20)
    Phone = models.CharField(max_length = 12)
    IsMale = models.BooleanField()
    BirthDate=models.CharField(max_length = 10)
    Email = models.CharField(max_length = 30)
    FavoriteLaundry = models.TextField()
    FavoriteRepair = models.TextField()

    def __str__(self):
        return self.Name
