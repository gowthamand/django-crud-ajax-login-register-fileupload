from django.db import models
     
    # Create your models here.
     
class Member(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    created_at = models.CharField(max_length=40)
    updated_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.CharField(max_length=255, )
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
class Ajax(models.Model):
    text = models.CharField(max_length=255, blank=True)
    search = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)    
    url = models.URLField(max_length=200)
    telephone = models.IntegerField()
    password = models.CharField(max_length=20)
    number = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    
class Music(models.Model):    
    db_table = 'music_album'
    name = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
