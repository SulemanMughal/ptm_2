from django.db import models
from django.contrib.auth.models import User

CHOICES_TYPE=(
    ('In Creation','In Creation'),
    ('Requested','Requested'),
    ('Scheduled','Scheduled'),
    ('Cancelled','Cancelled'),
)

class properties(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    city = models.CharField(max_length=100,blank=True)
    area = models.CharField(max_length=100,blank=True)
    address = models.CharField(max_length=200,blank=True)
    price = models.IntegerField(default=0)
    sqft = models.FloatField(default=0)
    beds = models.IntegerField(default=0)
    baths = models.IntegerField(default=0)
    family_type = models.CharField(max_length=100,blank=True)
    year_built = models.IntegerField(default=2020)
    heating = models.CharField(max_length=100,blank=True)
    cooling = models.CharField(max_length=100,blank=True)
    parking = models.IntegerField(default=0)
    lot = models.IntegerField(default=0)
    description = models.TextField(max_length=2000,blank=True)
    image1 = models.ImageField(blank=True)
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)
    image4 = models.ImageField(blank=True)
    image5 = models.ImageField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.user.username + ' has property worth ' + str(self.price))

class shortlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    name = models.CharField(max_length=100,blank=True)
    relproperties = models.ManyToManyField(properties,blank=True)
    note = models.TextField(max_length=2000,blank=True)
    shared_with = models.ManyToManyField(User,related_name='shared_with')
    linked_with = models.ManyToManyField(User,blank=True,related_name='linked_with')

    def __str__(self):
        return (self.name)

class propertyrating(models.Model):
    linklist = models.ForeignKey(shortlist,on_delete=models.CASCADE)
    relproperty = models.ForeignKey(properties,on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

class notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,related_name='user')
    relproperty = models.ForeignKey(properties,on_delete=models.CASCADE,blank=True,related_name='relproperty')
    relshortlist = models.ForeignKey(shortlist,on_delete=models.CASCADE,null=True,related_name='relshortlist')
    note = models.TextField(max_length=2000,blank=True)

    def __str__(self):
        return (self.note)

class tourrequests(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,related_name='usertr')
    relproperty = models.ManyToManyField(properties,blank=True,related_name='relpropertytr')
    name = models.CharField(max_length=50)
    date1 = models.CharField(max_length=200,blank=True)
    time1_date1 = models.CharField(max_length=200,blank=True)
    time2_date1 = models.CharField(max_length=200,blank=True)
    time3_date1 = models.CharField(max_length=200,blank=True)
    date2 = models.CharField(max_length=200,blank=True)
    time1_date2 = models.CharField(max_length=200,blank=True)
    time2_date2 = models.CharField(max_length=200,blank=True)
    time3_date2 = models.CharField(max_length=200,blank=True)
    date3 = models.CharField(max_length=200,blank=True)
    time1_date3 = models.CharField(max_length=200,blank=True)
    time2_date3 = models.CharField(max_length=200,blank=True)
    time3_date3 = models.CharField(max_length=200,blank=True)
    status = models.CharField(max_length=20, blank=True, default='In Creation' ,choices=CHOICES_TYPE)
    note = models.TextField(max_length=1000,blank=True)

    def __str__(self):
        return (self.name + ' by ' + self.user.username + ' : ' + self.status)

class offers(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True)
    relproperty = models.ForeignKey(properties,on_delete=models.CASCADE,blank=True)
    note = models.CharField(max_length=200,blank=True)
    status = models.CharField(max_length=50,default='Submitted')

    def __str__(self):
        return self.note