# Generated by Django 4.0.5 on 2022-07-25 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMS', '0003_course_students_alter_paymentdetials_payment_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
