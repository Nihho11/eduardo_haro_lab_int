# Generated by Django 4.2.1 on 2023-05-12 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Owner',
        ),
    ]