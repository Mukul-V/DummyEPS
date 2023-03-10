# Generated by Django 4.1.6 on 2023-02-05 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('epsapp', '0034_tokenauth_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserHardwareRestrict',
            fields=[
                ('key', models.AutoField(primary_key=True, serialize=False)),
                ('hardware_value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsapp.hardware', verbose_name='hardware_value')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsapp.users')),
            ],
            options={
                'verbose_name_plural': 'User Hardware Restrict',
            },
        ),
    ]
