# Generated by Django 4.0.6 on 2022-07-25 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tekylearn', '0018_learn_prize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learn_prize',
            name='img',
            field=models.ImageField(upload_to='images/test'),
        ),
    ]