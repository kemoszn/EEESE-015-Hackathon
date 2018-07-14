from django.db import models


class Admission(models.Model):
    name = models.CharField(max_length=20)
    index = models.IntegerField()
    email = models.EmailField()
    publish = models.DateTimeField(auto_now_add=True)
    Request = models.TextField(max_length=140)
    
    
    def __str__(self):
        return self.name 
    
    
    
