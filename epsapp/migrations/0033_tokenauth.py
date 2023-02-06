# Generated by Django 4.1.6 on 2023-02-05 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('epsapp', '0032_webdlp_custom_alter_webdlpdata_action'),
    ]

    operations = [
        migrations.CreateModel(
            name='TokenAuth',
            fields=[
                ('key', models.AutoField(primary_key=True, serialize=False)),
                ('access_token', models.CharField(max_length=300, verbose_name='access_token')),
                ('refresh_token', models.CharField(max_length=300, verbose_name='refresh_token')),
                ('role', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.IntegerField()),
                ('admin_key', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='epsapp.admin', verbose_name='admin_key')),
                ('org_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsapp.organization', verbose_name='organization_key')),
            ],
            options={
                'verbose_name_plural': 'Token Authentication',
            },
        ),
    ]
