# Generated by Django 4.1.6 on 2023-02-04 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('epsapp', '0006_baseclassificationgroup_appcontrolpolicydata_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseclassificationgroup',
            name='organization',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='epsapp.organization'),
        ),
    ]