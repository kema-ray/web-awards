# Generated by Django 4.0.5 on 2022-06-12 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myawwards', '0006_rename_content_rate_rating_content_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='overall_score',
            new_name='score',
        ),
    ]
