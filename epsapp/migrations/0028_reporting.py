# Generated by Django 4.1.6 on 2023-02-05 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('epsapp', '0027_ostable'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reporting',
            fields=[
                ('key', models.AutoField(primary_key=True, serialize=False)),
                ('incident_time', models.DateTimeField()),
                ('source', models.CharField(max_length=100)),
                ('endpoint', models.CharField(max_length=200, null=True)),
                ('policy', models.CharField(max_length=100)),
                ('channel', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1)),
                ('destination', models.CharField(max_length=100)),
                ('transaction_size', models.CharField(max_length=50)),
                ('action', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=2)),
                ('maximum_matches', models.IntegerField()),
                ('status', models.CharField(default='new', max_length=50)),
                ('severity', models.CharField(default='low', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('detected_by', models.CharField(max_length=50)),
                ('files', models.CharField(max_length=100, null=True)),
                ('application_name', models.CharField(max_length=100)),
                ('direction', models.CharField(default='inbound', max_length=100)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsapp.organization')),
            ],
            options={
                'verbose_name_plural': 'Reporting',
            },
        ),
    ]