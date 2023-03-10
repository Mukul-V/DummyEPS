# Generated by Django 4.1.6 on 2023-02-05 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epsapp', '0024_localprinterdlp'),
    ]

    operations = [
        migrations.AddField(
            model_name='antivirus',
            name='custom',
            field=models.IntegerField(choices=[(0, 0), (1, 1)], default=1),
        ),
        migrations.AddField(
            model_name='appcontrolpolicy',
            name='custom',
            field=models.IntegerField(choices=[(0, 0), (1, 1)], default=1),
        ),
        migrations.AddField(
            model_name='appfileaccessdlp',
            name='custom',
            field=models.IntegerField(choices=[(0, 0), (1, 1)], default=1),
        ),
        migrations.AddField(
            model_name='appversion',
            name='custom',
            field=models.IntegerField(choices=[(0, 0), (1, 1)], default=1),
        ),
        migrations.AddField(
            model_name='clipboarddlp',
            name='custom',
            field=models.IntegerField(choices=[(0, 0), (1, 1)], default=1),
        ),
        migrations.AddField(
            model_name='contentclassification',
            name='custom',
            field=models.IntegerField(choices=[(0, 0), (1, 1)], default=1),
        ),
        migrations.AddField(
            model_name='localprinterdlp',
            name='custom',
            field=models.IntegerField(choices=[(0, 0), (1, 1)], default=1),
        ),
        migrations.AddField(
            model_name='role',
            name='custom',
            field=models.IntegerField(choices=[(0, 0), (1, 1)], default=1),
        ),
    ]
