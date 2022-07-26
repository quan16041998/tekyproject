# Generated by Django 4.0.6 on 2022-07-27 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tekylearn', '0030_trungtam'),
    ]

    operations = [
        migrations.CreateModel(
            name='CapHoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RegisterStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=11)),
                ('caphoc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test', to='tekylearn.caphoc')),
                ('trungtam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test', to='tekylearn.trungtam')),
            ],
        ),
    ]
