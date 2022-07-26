# Generated by Django 4.0.6 on 2022-07-21 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tekylearn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='teacher_number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title_smail', models.CharField(max_length=100)),
                ('title_big', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='hoconline',
            name='subject',
            field=models.CharField(max_length=50),
        ),
    ]
