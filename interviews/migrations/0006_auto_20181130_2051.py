# Generated by Django 2.1 on 2018-11-30 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interviews', '0005_auto_20181130_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(),
        ),
    ]