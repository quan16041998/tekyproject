# Generated by Django 4.0.6 on 2022-07-27 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tekylearn', '0029_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='trungtam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
