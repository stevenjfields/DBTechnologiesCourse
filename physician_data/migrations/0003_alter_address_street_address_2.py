# Generated by Django 4.0.6 on 2022-07-29 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('physician_data', '0002_alter_address_physician_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='Street_Address_2',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
