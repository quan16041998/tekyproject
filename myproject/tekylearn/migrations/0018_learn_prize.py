# Generated by Django 4.0.6 on 2022-07-25 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tekylearn', '0017_rename_title_smail_title_title_small'),
    ]

    operations = [
        migrations.CreateModel(
            name='learn_prize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='images/upload')),
            ],
        ),
    ]
