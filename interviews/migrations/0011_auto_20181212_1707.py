# Generated by Django 2.1 on 2018-12-12 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interviews', '0010_favorite'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favorite',
            options={'ordering': ['-created']},
        ),
    ]
