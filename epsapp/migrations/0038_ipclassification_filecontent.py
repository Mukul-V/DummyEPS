# Generated by Django 4.1.6 on 2023-02-05 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('epsapp', '0037_users_user_group_mapping'),
    ]

    operations = [
        migrations.CreateModel(
            name='IpClassification',
            fields=[
                ('key', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('type', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=1)),
                ('startIp', models.GenericIPAddressField(default='0.0.0.0', null=True)),
                ('endIp', models.GenericIPAddressField(default='0.0.0.0', null=True)),
                ('subnetMask', models.IntegerField(default=0, null=True)),
                ('ipList', models.CharField(default='0.0.0.0', max_length=1000, null=True)),
                ('custom', models.IntegerField(choices=[(0, 0), (1, 1)], default=1)),
                ('class_super', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsapp.classificationsuperclass')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsapp.organization')),
            ],
            options={
                'verbose_name_plural': 'Ip FileClassification',
            },
        ),
        migrations.CreateModel(
            name='FileContent',
            fields=[
                ('key', models.AutoField(primary_key=True, serialize=False)),
                ('file_row', models.CharField(max_length=150)),
                ('file_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsapp.contentclassification')),
            ],
            options={
                'verbose_name_plural': 'File Content',
            },
        ),
    ]