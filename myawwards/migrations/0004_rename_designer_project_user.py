# Generated by Django 4.0.5 on 2022-06-11 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myawwards', '0003_project_designer_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='designer',
            new_name='user',
        ),
    ]
