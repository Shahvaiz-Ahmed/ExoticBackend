# Generated by Django 5.0.2 on 2024-07-24 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bccustomer',
            name='No',
            field=models.CharField(max_length=110, unique=True),
        ),
        migrations.AlterField(
            model_name='bccustomer',
            name='PhoneNo',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='bccustomer',
            name='ShiptoCode',
            field=models.CharField(max_length=100),
        ),
    ]
