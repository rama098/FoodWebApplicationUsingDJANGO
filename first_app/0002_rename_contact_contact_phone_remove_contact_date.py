# Generated by Django 4.1.5 on 2023-03-23 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='contact',
            new_name='phone',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='date',
        ),
    ]