# Generated by Django 3.0 on 2020-11-22 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentrecords',
            name='bookIssued',
        ),
    ]
