# Generated by Django 4.0.2 on 2022-03-17 19:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobilenumber', '0006_alter_phonemodel_date_reported_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonemodel',
            name='date_reported',
            field=models.DateField(default=datetime.datetime(2022, 3, 18, 0, 2, 33, 891807)),
        ),
        migrations.AlterField(
            model_name='reviewmodel',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 18, 0, 2, 34, 35805)),
        ),
    ]
