# Generated by Django 2.1.7 on 2019-10-01 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0005_auto_20191001_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_service',
            name='delivery_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]