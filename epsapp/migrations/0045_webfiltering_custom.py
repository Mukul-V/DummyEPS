# Generated by Django 4.1.6 on 2023-02-06 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epsapp', '0044_rename_appclassdata_appclassificationdata_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='webfiltering',
            name='custom',
            field=models.IntegerField(choices=[(0, 0), (1, 1)], default=1),
        ),
    ]