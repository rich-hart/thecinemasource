# Generated by Django 2.1 on 2018-12-01 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interviews', '0007_auto_20181201_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.TextField(),
        ),
    ]
