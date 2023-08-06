from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    age = models.IntegerField()
    
    def __str__(self):
        return f'{self.fname} {self.lname}'
    
    def get_id(self):
        return f'User ID: {self.id}, User name: {self.fname} {self.lname} Age: {self.age}'
    
    @staticmethod
    def sum():
        total_sum = User.objects.aggregate(models.Sum('age'))['age__sum']
        return total_sum