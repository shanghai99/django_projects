# Generated by Django 3.1.1 on 2020-11-06 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='description',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='site',
            name='justification',
            field=models.CharField(max_length=128),
        ),
    ]