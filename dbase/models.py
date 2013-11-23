from django.db import models

# Create your models here.
class Merchant_Unit(models.Model):
    def __unicode__(self):
            return self.title
    mid = models.IntegerField(primary_key=True)#Merchant iD
    sid = models.IntegerField()#Website ID
    cid = models.IntegerField()#City ID
    mcid = models.IntegerField()#Merchant Category ID
    name = models.CharField(max_length=90)#Merchant Name
    addr = models.CharField(max_length=90)#Merchant Address
    logo = models.ImageField(upload_to = 'Merchant_Logo')
    detail = models.TextField()
    link = models.URLField()
class Website_Unit(models.Model):
    def __unicode__(self):
            return self.title
    sid = models.IntegerField(primary_key=True)#Website ID
    link = models.URLField()
    name = models.CharField(max_length=90)
    since = models.DateTimeField(auto_now=True)#Setup Date
class Item_Unit(models.Model):
    def __unicode__(self):
            return self.title
    mid = models.IntegerField()
    id = models.IntegerField(primary_key=True)#Item ID
    icid = models.IntegerField()#Item Category ID 
    name =  models.CharField(max_length=90)
    regular =  models.CharField(max_length=90)#Regular Detail
    avmount = models.IntegerField()#Available Amount Number??
    detail = models.TextField()
    link = models.URLField()
    price = models.IntegerField()
    ori_price = models.IntegerField()
    since = models.DateTimeField(auto_now=True)#Setup Date
class City(models.Model):
    def __unicode__(self):
            return self.title
    cid = models.IntegerField(primary_key=True)#City ID
    name = models.CharField(max_length=90)
    state = models.CharField(max_length=90)
class Merchant_Category(models.Model):
    def __unicode__(self):
            return self.title
    mcid = models.IntegerField(primary_key=True)
    supid = models.IntegerField()#Parent Category ID
    name = models.CharField(max_length=90)
    detail = models.TextField()
class Item_Category(models.Model):
    def __unicode__(self):
            return self.title
    icid = models.IntegerField(primary_key=True)
    supid = models.IntegerField()
    name = models.CharField(max_length=90)
    detail = models.TextField()
class Avatar_Base(models.Model):
    def __unicode__(self):
            return self.title
    aid = models.IntegerField(primary_key=True)#Avatar ID
    id = models.IntegerField()#Item ID of the Avatar
    avatar = models.ImageField(upload_to='Avatar')





