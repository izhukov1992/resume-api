# Generated by Django 2.0.1 on 2018-01-12 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_account_userpic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='userpic',
            field=models.ImageField(upload_to='resume'),
        ),
    ]
