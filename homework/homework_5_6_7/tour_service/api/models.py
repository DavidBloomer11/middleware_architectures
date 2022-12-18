from django.db import models
import hashlib

# Create your models here.
class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    code = models.CharField(max_length=2)

    class Meta:
        managed = True
        db_table = 'country'
    
    def __str__(self):
        return self.name

class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    street = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    country = models.ForeignKey(Country,on_delete = models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'location'
    
    def __str__(self):
        return self.name

class Tour(models.Model):
    tour_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location,on_delete =models.DO_NOTHING)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'tour'
    
    def __str__(self):
        return self.name


    def get_hash(self):
        string = self.name + self.location.name + str(self.tour_id)
        hash = hashlib.md5(string.encode('utf-8'))
        return hash.hexdigest()

    def get_weak_etag():
        tour_list = Tour.objects.all()
        string = ''
        for tour in tour_list:
            string += tour.name + str(tour.tour_id)
        hash = hashlib.md5(string.encode('utf-8'))
        return hash.hexdigest()

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    identification_number = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'customer'
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name


class CustomerOnTour(models.Model):
    customer_on_tour_id = models.AutoField(primary_key=True)
    tour = models.ForeignKey(Tour,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    date_start = models.DateField(null=True,blank=True)
    date_end = models.DateField(null=True,blank=True)

    class Meta:
        managed = True
        db_table = 'customer_on_tour'
    
    def __str__(self):
        return self.customer.first_name + ' ' + self.customer.last_name + ' - tour: ' + self.tour.name

