# Generated by Django 4.0.5 on 2022-06-12 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myawwards', '0008_profile_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]