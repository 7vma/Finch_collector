# Generated by Django 4.1.1 on 2022-10-03 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_artist_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='img',
            field=models.CharField(default='avatar.png', max_length=500),
        ),
    ]