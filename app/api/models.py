from django.db import models


class Breed(models.Model):
    SIZE_CHOICES = [
        ('Tiny', 'Tiny'),
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    ]
    RATING_CHOICES = [(i, i) for i in range(1, 6)]

    name = models.CharField(max_length=100)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    friendliness = models.IntegerField(choices=RATING_CHOICES)
    trainability = models.IntegerField(choices=RATING_CHOICES)
    shedding_amount = models.IntegerField(choices=RATING_CHOICES)
    exercise_needs = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return self.name


class Dog(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    color = models.CharField(max_length=50)
    favorite_food = models.CharField(max_length=100)
    favorite_toy = models.CharField(max_length=100)

    def __str__(self):
        return self.name
