# Generated by Django 2.1.1 on 2018-11-26 10:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=250)),
                ('time_stamp', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_content', models.TextField(default='SOME_TEXT', help_text='Whats on your mind?', max_length=500)),
                ('img_content', models.ImageField(default='SOME_IMG', upload_to=None)),
                ('time_stamp', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(blank=True)),
                ('status', models.CharField(blank=True, choices=[('0', 'None'), ('1', 'React 1'), ('2', 'React 2'), ('3', 'React 3'), ('4', 'React 4')], default='0', max_length=1)),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='closeknit.Post')),
            ],
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend_code', models.CharField(max_length=20)),
                ('friends', models.ManyToManyField(blank=True, default=None, related_name='_useraccount_friends_+', to='closeknit.UserAccount')),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='reaction',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='closeknit.UserAccount'),
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='closeknit.UserAccount'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='closeknit.UserAccount'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='closeknit.Post'),
        ),
    ]
