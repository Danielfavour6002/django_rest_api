# Generated by Django 5.0.6 on 2024-05-26 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_registration_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
    ]
