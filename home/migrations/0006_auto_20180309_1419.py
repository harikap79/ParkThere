# Generated by Django 2.0.2 on 2018-03-09 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20180307_0034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmarkedcarpark',
            name='carpark_ptr',
        ),
        migrations.RemoveField(
            model_name='bookmarkedcarpark',
            name='user',
        ),
        migrations.RemoveField(
            model_name='searchhistory',
            name='carpark_ptr',
        ),
        migrations.RemoveField(
            model_name='searchhistory',
            name='user',
        ),
        migrations.DeleteModel(
            name='BookmarkedCarPark',
        ),
        migrations.DeleteModel(
            name='SearchHistory',
        ),
    ]
