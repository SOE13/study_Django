from django.db import models

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=100,null=False)
    writer_name=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name
    

class Writer(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)

    def __str__(self):
        return self.first_name +' '+ self.last_name