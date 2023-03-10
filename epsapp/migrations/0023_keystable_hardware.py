# Generated by Django 4.1.6 on 2023-02-05 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('epsapp', '0022_fileclassification'),
    ]

    operations = [
        migrations.CreateModel(
            name='KeysTable',
            fields=[
                ('key', models.AutoField(primary_key=True, serialize=False)),
                ('key_value', models.CharField(max_length=200)),
                ('issue_date', models.DateField()),
                ('tenure_type', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)], default=0)),
                ('activate_date', models.DateField(null=True)),
                ('grace_period', models.IntegerField(default=10)),
                ('tenure_value', models.IntegerField(null=True)),
                ('expiry_date', models.DateField(null=True)),
                ('status', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=0)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsapp.organization')),
            ],
        ),
        migrations.CreateModel(
            name='Hardware',
            fields=[
                ('key', models.AutoField(primary_key=True, serialize=False)),
                ('hardware_value', models.CharField(max_length=250)),
                ('bandwidth', models.CharField(max_length=100, null=True)),
                ('cpu', models.CharField(max_length=100, null=True)),
                ('ram', models.CharField(max_length=100, null=True)),
                ('hdd', models.CharField(max_length=100, null=True)),
                ('current_wifi', models.CharField(max_length=100, null=True)),
                ('current_ip', models.CharField(max_length=300, null=True)),
                ('key_value', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='epsapp.keystable')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsapp.organization')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='epsapp.users')),
            ],
            options={
                'verbose_name_plural': 'Hardware Table',
            },
        ),
    ]
