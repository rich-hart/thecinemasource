# Generated by Django 2.1 on 2018-12-02 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interviews', '0008_auto_20181201_2141'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['title']},
        ),
    ]