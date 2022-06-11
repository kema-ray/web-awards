# Generated by Django 4.0.5 on 2022-06-11 14:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myawwards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='project',
            name='technologies',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]