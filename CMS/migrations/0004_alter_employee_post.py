# Generated by Django 4.0.5 on 2022-07-08 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMS', '0003_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='post',
            field=models.CharField(max_length=20),
        ),
    ]