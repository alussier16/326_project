# Generated by Django 2.1.1 on 2018-10-31 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('closeknit', '0025_post_img_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reaction',
            name='status',
            field=models.CharField(blank=True, choices=[('0', 'None'), ('1', 'React 1'), ('2', 'React 2'), ('3', 'React 3'), ('4', 'React 4')], default='0', max_length=1),
        ),
    ]
