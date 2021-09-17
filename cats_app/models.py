from django.db import models


class Colors(models.TextChoices):
    b = 'black'
    w = 'white'
    bw = 'black & white'
    r = 'red'
    rw = 'red & white'
    rbw = 'red & black & white'


# class Cats(models.Model):
#     name = models.TextField( max_length=20)
#     color = models.CharField(choices=Colors.choices, max_length=30)
#     tail_length = models.IntegerField()
#     whiskers_length = models.IntegerField()
class Cats(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    color = models.CharField(choices=Colors.choices, max_length=30)
    tail_length = models.IntegerField(blank=False)
    whiskers_length = models.IntegerField(blank=False)

    class Meta:
        managed = False
        db_table = 'cats'



class CatColorsInfo(models.Model):
    color = models.CharField(choices=Colors.choices, max_length=30)
    count = models.IntegerField(blank=False, null=True)

    class Meta:
        managed = False
        db_table = 'cat_colors_info'


class CatsStat(models.Model):
    tail_length_mean = models.IntegerField(primary_key=True)
    tail_length_median = models.IntegerField()
    tail_length_mode = models.IntegerField()
    whiskers_length_mean = models.IntegerField()
    whiskers_length_median = models.IntegerField()
    whiskers_length_mode = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cats_stat'

