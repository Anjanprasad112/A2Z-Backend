# Generated by Django 4.2.3 on 2023-07-13 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('A2Zbackend', '0006_remove_company_free_trial_date_left'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicles',
            name='vehicle_type',
            field=models.IntegerField(max_length=100),
        ),
    ]