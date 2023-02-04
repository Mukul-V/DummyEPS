# Generated by Django 4.1.6 on 2023-02-04 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nividapp', '0014_delete_ourclients'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppControlPolicy',
            fields=[
                ('key', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nividapp.organization')),
            ],
            options={
                'verbose_name_plural': 'App Control Policy',
                'get_latest_by': 'key',
            },
        ),
    ]
