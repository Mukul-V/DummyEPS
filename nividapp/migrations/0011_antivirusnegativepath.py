# Generated by Django 4.1.6 on 2023-02-04 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nividapp', '0010_delete_randommodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='AntivirusNegativePath',
            fields=[
                ('key', models.AutoField(primary_key=True, serialize=False)),
                ('negative_path', models.CharField(max_length=200)),
                ('antivirus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nividapp.antivirus')),
            ],
            options={
                'verbose_name_plural': 'Antivirus Negative path Model',
            },
        ),
    ]
