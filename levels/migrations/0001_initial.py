# Generated by Django 4.0.3 on 2022-03-26 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calid', models.CharField(max_length=100)),
                ('corid', models.CharField(max_length=100)),
                ('estacion_id', models.CharField(max_length=100)),
                ('model_name', models.CharField(max_length=100)),
                ('cal_name', models.CharField(max_length=100)),
                ('label', models.CharField(max_length=100)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('value', models.DecimalField(decimal_places=4, max_digits=5)),
            ],
        ),
    ]