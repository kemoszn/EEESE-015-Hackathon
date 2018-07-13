from django.db import models
from django.utils import timezone


class Event(models.Model):
    DEPARTMENT_CHOICES = (
        ('Electrical','electrical'),
        ('Civil','civil'),
        ('Chemical','chemical'),
    )
    #image = models.ImageField(upload_to='static/feed/images/')
    author = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=30)
    date = models.DateTimeField()
    department = models.CharField(max_length=10, choices=DEPARTMENT_CHOICES)
    place = models.CharField(max_length=10)
    slug = models.SlugField(max_length=250, unique_for_date='date')
    
    
    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.name
    



class New(models.Model):
    DEPARTMENT_CHOICES = (
        ('Electrical','electrical'),
        ('Civil','civil'),
        ('Chemical','chemical'),
        ('Global','global'),
    )
    
    body = models.TextField(max_length=200)
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    publish = models.DateTimeField()
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    description = models.CharField(max_length=10, choices=DEPARTMENT_CHOICES, default='Global')
    
    class Meta: 
        ordering = ('-publish',)
        
        
    def __str__(self):
        return self.title
    

    
    
    
    
    