# Generated by Django 2.1 on 2018-11-30 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interviews', '0004_remove_post_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
