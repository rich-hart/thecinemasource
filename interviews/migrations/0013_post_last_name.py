# Generated by Django 2.1 on 2018-12-14 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interviews', '0012_post_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='last_name',
            field=models.CharField(default='*', max_length=255),
            preserve_default=False,
        ),
    ]
