from django.db import models

# Create your models here.
class Level(models.Model):
    calid = models.CharField(max_length=100)
    corid = models.CharField(max_length=100)
    estacion_id = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    cal_name = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    forecast_date = models.DateField
    create_date = models.DateTimeField(auto_now_add = True)
    value_date = models.DateField
    value = models.DecimalField(max_digits=5, decimal_places=4)