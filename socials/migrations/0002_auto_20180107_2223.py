# Generated by Django 2.0.1 on 2018-01-07 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='social',
            name='type',
            field=models.CharField(choices=[(1, 'LinkedIn'), (2, 'GitHub'), (3, 'Upwork')], max_length=255),
        ),
    ]
