# Generated by Django 3.2.24 on 2024-02-19 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0007_auto_20240219_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmember',
            name='nickname',
            field=models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='닉네임'),
        ),
        migrations.AlterField(
            model_name='boardmember',
            name='userid',
            field=models.CharField(max_length=20, verbose_name='유저ID'),
        ),
    ]
