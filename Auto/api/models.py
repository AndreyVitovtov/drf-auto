from django.db import models


# Create your models here.

class Auto(models.Model):
    label = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.label


class Owner(models.Model):
    first_name = models.CharField(max_length=23)
    last_name = models.CharField(max_length=23)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class AutosPassport(models.Model):
    related_auto = models.ForeignKey(Auto, on_delete=models.CASCADE),
    prefix = models.TextField(max_length=2)
    number = models.CharField(max_length=6)

    def __str__(self):
        return f"{self.prefix} {self.number}"
