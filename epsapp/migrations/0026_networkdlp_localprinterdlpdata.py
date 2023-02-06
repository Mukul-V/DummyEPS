# Generated by Django 4.1.6 on 2023-02-05 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('epsapp', '0025_antivirus_custom_appcontrolpolicy_custom_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkDlp',
            fields=[
                ('key', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('custom', models.IntegerField(choices=[(0, 0), (1, 1)], default=1)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsapp.organization')),
            ],
            options={
                'verbose_name_plural': 'Network Dlp',
                'get_latest_by': 'key',
            },
        ),
        migrations.CreateModel(
            name='LocalPrinterDlpData',
            fields=[
                ('key', models.AutoField(primary_key=True, serialize=False)),
                ('action', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=2)),
                ('device_class_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='device_class_group_print', to='epsapp.baseclassificationgroup')),
                ('file_class_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file_class_group_print', to='epsapp.baseclassificationgroup')),
                ('local_printer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsapp.localprinterdlp')),
                ('schedule_class_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule_class_group_print', to='epsapp.baseclassificationgroup')),
            ],
            options={
                'verbose_name_plural': 'Local Printer Dlp Data',
            },
        ),
    ]
