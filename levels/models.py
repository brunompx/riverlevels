from django.db import models

# Create your models here.
class Level(models.Model):
    calid = models.CharField(max_length=100, null=True, blank=True)
    corid = models.CharField(max_length=100, null=True, blank=True)
    estacion_id = models.CharField(max_length=100, null=True, blank=True)
    model_name = models.CharField(max_length=100, null=True, blank=True)
    cal_name = models.CharField(max_length=100, null=True, blank=True)
    label = models.CharField(max_length=100, null=True, blank=True)
    forecast_date = models.DateField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add = True)
    value_date = models.DateField(null=True, blank=True)
    value = models.DecimalField(max_digits=5, decimal_places=4, null=True, blank=True)