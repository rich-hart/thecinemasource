# Generated by Django 2.1 on 2018-12-14 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interviews', '0013_post_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='index',
            field=models.CharField(choices=[('', 'NONE'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J'), ('K', 'K'), ('L', 'L'), ('M', 'M'), ('N', 'N'), ('O', 'O'), ('P', 'P'), ('Q', 'Q'), ('R', 'R'), ('S', 'S'), ('T', 'T'), ('U', 'U'), ('V', 'V'), ('W', 'W'), ('X', 'X'), ('Y', 'Y'), ('Z', 'Z')], max_length=1, null=True),
        ),
    ]