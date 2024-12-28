from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class notes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=1000)
    description=models.TextField()
    
    class Meta:
        verbose_name='notes'
        verbose_name_plural='notes'
    
    def __str__(self):
        return self.title
    
class homework(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    subject=models.CharField(max_length=1000)
    title=models.CharField(max_length=1000)
    description=models.TextField()
    due=models.DateTimeField(default=timezone.now())
    is_finished=models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.title
    
    
class Todo(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    is_finished=models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    