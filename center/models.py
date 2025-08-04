from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=52)

    def __str__(self):
        return self.name

class Oquv_markaz(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    number_of_teacher = models.DecimalField(max_digits=6, decimal_places=0)
    number_of_students = models.DecimalField(max_digits=6, decimal_places=0)
    desc = models.TextField()
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
# Create your models here.
