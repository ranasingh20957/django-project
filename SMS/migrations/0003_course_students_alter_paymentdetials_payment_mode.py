# Generated by Django 4.0.5 on 2022-07-23 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMS', '0002_course_paymentdetials'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, null=True, to='SMS.student'),
        ),
        migrations.AlterField(
            model_name='paymentdetials',
            name='payment_mode',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Debit Card', 'Debit Card'), ('Credit Card', 'Credit Card'), ('Paytm', 'Paytm')], max_length=100),
        ),
    ]
