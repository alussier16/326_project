# Generated by Django 2.1.1 on 2018-10-14 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('closeknit', '0002_auto_20181014_0350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='closeknit.User'),
        ),
    ]
