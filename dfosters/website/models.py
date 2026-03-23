from django.db import models

class reviews(models.Model):
    name= models.CharField(max_length=20)
    message = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name 
    

    
class Project(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects/')
    completed = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class Consultation(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Estimate(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    service = models.CharField(max_length=100)
    location = models.CharField(max_length=150, blank=True)
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service}"