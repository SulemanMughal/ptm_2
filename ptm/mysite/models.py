from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model

CHOICES_TYPE = (
    ('Buyer', 'Buyer'),
    ('Agent', 'Agent')
)

choice1 =(('Short Commute to work','Short Commute to work'),
          ('Access to shopping','Access to shopping'),
          ('Vastu Preference','Vastu Preference'),
          ('School Requirements','School Requirements'),
           )


class profileModel(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
    approve = models.BooleanField(default=True)
    Teacher_or_Parent = models.CharField(max_length=10, blank=True, default='Buyer' ,choices=CHOICES_TYPE)
    phone=models.CharField(max_length=11,blank=True,null=True, default='')
    occupation=models.CharField(max_length=200,blank=True,null=True, default='')
    #Property Requirements
    minprice = models.IntegerField(default=0)
    maxprice = models.IntegerField(default=0)
    minsqft = models.IntegerField(default=0)
    maxsqft = models.IntegerField(default=0)
    has_pre_approval=models.CharField(max_length=200,blank=True,null=True)
    property_type=models.CharField(max_length=200,blank=True,null=True)
    beds=models.CharField(max_length=200,blank=True,null=True)
    bath=models.CharField(max_length=200,blank=True,null=True)
    minlot = models.IntegerField(default=0)
    maxlot = models.IntegerField(default=0)
    stories=models.CharField(max_length=200,blank=True,null=True)
    location_preference=models.CharField(max_length=200,blank=True,null=True)
    looking_to_buy_in_how_many_months=models.CharField(max_length=200,blank=True,null=True)
    How_long_have_you_been_house_hunting=models.CharField(max_length=200,blank=True,null=True)
    Life_style = models.CharField(max_length=200,blank=True,null=True,choices=choice1)
    any_other = models.CharField(max_length=200,blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)


