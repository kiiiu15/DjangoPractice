from django.db import models


# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=50, default='')
    lastName = models.CharField(max_length=50, default='')
    age = models.IntegerField(default=0)

    def __str__(self):
        return '{"name": "%s", "lastName" : "%s", "age" : "%d"}' % (self.name, self.lastName, self.age)


class Pet(models.Model):
    name = models.CharField(max_length=50)
    weight = models.IntegerField(default=0)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return '{"name": "%s", "weight" : "%d", "owner" : "%s"}' % (self.name, self.weight, self.owner.__str__())
