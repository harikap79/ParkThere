# Generated by Django 2.0.2 on 2018-03-26 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20180321_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='carpark',
            name='x',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carpark',
            name='y',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
