# Generated by Django 4.1.6 on 2023-02-26 17:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='datetime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 2, 26, 17, 9, 40, 220732, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='email',
            field=models.EmailField(max_length=120),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='phonenumber',
            field=models.IntegerField(),
        ),
    ]