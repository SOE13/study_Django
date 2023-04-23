from django.db import models

# Create your models here.


class Writer(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    age=models.CharField(max_length=2,null=True)

    def __str__(self):
        return self.first_name +' '+ self.last_name


class Book(models.Model):
    name=models.CharField(max_length=100,null=False)
    writer=models.ForeignKey(Writer, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name