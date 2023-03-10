# Generated by Django 4.1.6 on 2023-02-05 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('epsapp', '0029_roleandaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rules',
            fields=[
                ('key', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('position', models.IntegerField(default=0)),
                ('custom', models.IntegerField(choices=[(0, 0), (1, 1)], default=1)),
                ('app_control_policy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='epsapp.appcontrolpolicy')),
                ('app_file_access_dlp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='epsapp.appfileaccessdlp')),
                ('clipboard_dlp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='epsapp.clipboarddlp')),
                ('device_control_policy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='epsapp.devicecontrolpolicy')),
                ('local_printer_dlp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='epsapp.localprinterdlp')),
                ('network_dlp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='epsapp.networkdlp')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsapp.organization')),
            ],
            options={
                'verbose_name_plural': 'Rules',
                'get_latest_by': 'key',
            },
        ),
        migrations.CreateModel(
            name='ScheduleClassification',
            fields=[
                ('key', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('duration', models.IntegerField(choices=[(1, 1), (2, 2)], default=1)),
                ('custom', models.IntegerField(choices=[(0, 0), (1, 1)], default=1)),
                ('class_super', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='epsapp.classificationsuperclass')),
                ('organization', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='epsapp.organization')),
            ],
            options={
                'verbose_name_plural': 'Schedule FileClassification',
                'get_latest_by': 'key',
            },
        ),
        migrations.CreateModel(
            name='ScreenshotDlp',
            fields=[
                ('key', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('custom', models.IntegerField(choices=[(0, 0), (1, 1)], default=1)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsapp.organization')),
            ],
            options={
                'verbose_name_plural': 'Screenshot Dlp',
                'get_latest_by': 'key',
            },
        ),
        migrations.CreateModel(
            name='WebDlp',
            fields=[
                ('key', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsapp.organization')),
            ],
            options={
                'verbose_name_plural': 'Web Dlp',
                'get_latest_by': 'key',
            },
        ),
        migrations.CreateModel(
            name='WebFiltering',
            fields=[
                ('key', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('default_action', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=2)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsapp.organization')),
            ],
            options={
                'verbose_name_plural': 'Web Filtering',
                'get_latest_by': 'key',
            },
        ),
        migrations.CreateModel(
            name='WebFilteringMapping',
            fields=[
                ('key', models.AutoField(primary_key=True, serialize=False)),
                ('action', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=2)),
                ('schedule_class_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='epsapp.baseclassificationgroup')),
                ('web_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsapp.webclassification')),
                ('web_filter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsapp.webfiltering')),
            ],
            options={
                'verbose_name_plural': 'Web Filtering Mapping',
            },
        ),
        migrations.CreateModel(
            name='WebDlpData',
            fields=[
                ('key', models.AutoField(primary_key=True, serialize=False)),
                ('action', models.CharField(default='allow', max_length=10)),
                ('file_class_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file_class_group_web', to='epsapp.baseclassificationgroup')),
                ('schedule_class_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule_class_group_web', to='epsapp.baseclassificationgroup')),
                ('web_class_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='web_class_group_web', to='epsapp.baseclassificationgroup')),
                ('web_dlp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsapp.webdlp')),
            ],
            options={
                'verbose_name_plural': 'Web Dlp Data',
            },
        ),
        migrations.CreateModel(
            name='ScreenshotDlpData',
            fields=[
                ('key', models.AutoField(primary_key=True, serialize=False)),
                ('action', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=2)),
                ('app_class_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='app_class_group_scr', to='epsapp.baseclassificationgroup')),
                ('schedule_class_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule_class_group_scr', to='epsapp.baseclassificationgroup')),
                ('screenshot_dlp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsapp.screenshotdlp')),
            ],
            options={
                'verbose_name_plural': 'Screenshot Dlp Data',
            },
        ),
        migrations.CreateModel(
            name='ScheduleDays',
            fields=[
                ('key', models.AutoField(primary_key=True, serialize=False)),
                ('days', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=100)),
                ('schedule_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsapp.scheduleclassification')),
            ],
            options={
                'verbose_name_plural': 'Schedule Days',
                'get_latest_by': 'key',
            },
        ),
        migrations.CreateModel(
            name='RuleUserMapping',
            fields=[
                ('key', models.AutoField(primary_key=True, serialize=False)),
                ('rule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsapp.rules')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='epsapp.users')),
                ('user_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='epsapp.usergroup')),
            ],
            options={
                'verbose_name_plural': 'Rules User Mapping',
            },
        ),
        migrations.AddField(
            model_name='rules',
            name='screenshot_dlp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='epsapp.screenshotdlp'),
        ),
        migrations.AddField(
            model_name='rules',
            name='web_dlp',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='epsapp.webdlp'),
        ),
        migrations.AddField(
            model_name='rules',
            name='web_filter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='epsapp.webfiltering'),
        ),
        migrations.CreateModel(
            name='NetworkDlpData',
            fields=[
                ('key', models.AutoField(primary_key=True, serialize=False)),
                ('action', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=2)),
                ('file_class_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file_class_group_nwk', to='epsapp.baseclassificationgroup')),
                ('ip_class_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ip_class_group_nwk', to='epsapp.baseclassificationgroup')),
                ('network_dlp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='epsapp.networkdlp')),
                ('schedule_class_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule_class_group_nwk', to='epsapp.baseclassificationgroup')),
            ],
            options={
                'verbose_name_plural': 'Network Dlp Data',
            },
        ),
    ]
