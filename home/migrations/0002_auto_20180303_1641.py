# Generated by Django 2.0.2 on 2018-03-03 08:41

from django.db import migrations
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', home.models.UserManager()),
            ],
        ),
    ]
