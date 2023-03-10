# Generated by Django 4.1.6 on 2023-02-04 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('epsapp', '0014_classificationgroupmapping'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClipboardDlp',
            fields=[
                ('key', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=1000)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsapp.organization')),
            ],
            options={
                'verbose_name_plural': 'Clipboard Dlp',
                'get_latest_by': 'key',
            },
        ),
    ]
