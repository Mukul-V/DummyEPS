# Generated by Django 4.1.6 on 2023-02-06 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epsapp', '0047_admin_country_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='country_code',
            field=models.CharField(default='+00', max_length=3),
        ),
    ]
