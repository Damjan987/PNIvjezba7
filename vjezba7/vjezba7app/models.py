from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import render


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional
    nickname = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.user


# Create your models here.
class Projection(models.Model):
    film_name = models.CharField(max_length=100)
    film_duration = models.CharField(max_length=100)
    film_capacity = models.CharField(max_length=100)

    def __str__(self):
        return self.film_name

class Card(models.Model):
    film = models.ForeignKey(Projection, on_delete=models.CASCADE, related_name='cards')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=100)

    def __str__(self):
        return self.seat_number

    def get_absolute_url(self):
        return reverse("vjezba7app:list", kwargs={'pk':self.pk})