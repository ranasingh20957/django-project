# Generated by Django 4.0.5 on 2022-07-03 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('Address', models.CharField(max_length=100)),
                ('mobileno', models.CharField(max_length=15)),
            ],
        ),
    ]
