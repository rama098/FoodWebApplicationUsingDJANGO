# Generated by Django 4.1.5 on 2023-03-27 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_rename_contact_contact_phone_remove_contact_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name2', models.CharField(max_length=122)),
                ('email2', models.CharField(max_length=122)),
                ('phone2', models.CharField(max_length=12)),
            ],
        ),
    ]