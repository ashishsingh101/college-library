# Generated by Django 3.0 on 2020-11-22 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20201122_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentrecords',
            name='book1',
            field=models.CharField(default='None', max_length=50),
        ),
        migrations.AlterField(
            model_name='studentrecords',
            name='book2',
            field=models.CharField(default='None', max_length=50),
        ),
        migrations.AlterField(
            model_name='studentrecords',
            name='book3',
            field=models.CharField(default='None', max_length=50),
        ),
    ]
