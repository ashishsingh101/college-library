# Generated by Django 3.0 on 2020-11-22 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_remove_studentrecords_bookissued'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentrecords',
            name='book1',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='studentrecords',
            name='book2',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='studentrecords',
            name='book3',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]
