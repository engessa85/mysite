# Generated by Django 2.2.6 on 2019-10-04 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0009_auto_20191003_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_service',
            name='country',
            field=models.CharField(max_length=75, null=True),
        ),
        migrations.AlterField(
            model_name='user_service',
            name='email',
            field=models.CharField(max_length=75, null=True),
        ),
    ]