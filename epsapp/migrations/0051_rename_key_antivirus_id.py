# Generated by Django 4.1.6 on 2023-02-08 23:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('epsapp', '0050_rename_key_userauthentication_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='antivirus',
            old_name='key',
            new_name='id',
        ),
    ]
