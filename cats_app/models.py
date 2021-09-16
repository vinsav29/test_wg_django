from django.db import models


class Colors(models.TextChoices):
    b = 'black'
    w = 'white'
    bw = 'black & white'
    r = 'red'
    rw = 'red & white'
    rbw = 'red & black & white'


class Cats(models.Model):
    name = models.TextField()
    color = models.CharField(choices=Colors.choices)
    tail_length = models.IntegerField()
    whiskers_length = models.IntegerField()


class CatsColorsInfo(models.Model):
    color = models.CharField(choices=Colors.choices)
    count = models.IntegerField()


class CatsStat(models.Model):
    tail_length_mean = models.IntegerField()
    tail_length_median = models.IntegerField()
    tail_length_mode = models.IntegerField()
    whiskers_length_mean = models.IntegerField()
    whiskers_length_median = models.IntegerField()
    whiskers_length_mode = models.IntegerField()
