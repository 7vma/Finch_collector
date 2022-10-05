# Generated by Django 4.1.2 on 2022-10-05 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0005_playlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='artist',
            name='bio',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='artist',
            name='img',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]