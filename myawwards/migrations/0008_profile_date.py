# Generated by Django 4.0.5 on 2022-06-12 15:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myawwards', '0007_rename_overall_score_rating_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]