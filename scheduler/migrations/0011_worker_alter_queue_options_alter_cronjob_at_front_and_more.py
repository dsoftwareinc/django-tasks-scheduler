# Generated by Django 4.1.7 on 2023-04-03 00:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('scheduler', '0010_queue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': ' Workers',
                'permissions': [['view', 'Access admin page']],
                'managed': False,
                'default_permissions': (),
            },
        ),
        migrations.AlterModelOptions(
            name='queue',
            options={'default_permissions': (), 'managed': False, 'permissions': [['view', 'Access admin page']],
                     'verbose_name_plural': ' Queues'},
        ),
        migrations.AlterField(
            model_name='cronjob',
            name='at_front',
            field=models.BooleanField(blank=True, default=False,
                                      help_text='When queuing the job, add it in the front of the queue', null=True,
                                      verbose_name='At front'),
        ),
        migrations.AlterField(
            model_name='cronjob',
            name='cron_string',
            field=models.CharField(
                help_text='Define the schedule in a crontab like syntax.\n            Times are in UTC. Use <a href="https://crontab.guru/">crontab.guru</a> to create a cron string.',
                max_length=64, verbose_name='cron string'),
        ),
        migrations.AlterField(
            model_name='cronjob',
            name='enabled',
            field=models.BooleanField(default=True,
                                      help_text='Should job be scheduled? This field is useful to keep past jobs that should no longer be scheduled',
                                      verbose_name='enabled'),
        ),
        migrations.AlterField(
            model_name='cronjob',
            name='job_id',
            field=models.CharField(blank=True, editable=False, help_text='Current job_id on queue', max_length=128,
                                   null=True, verbose_name='job id'),
        ),
        migrations.AlterField(
            model_name='cronjob',
            name='queue',
            field=models.CharField(choices=[('default', 'default'), ('low', 'low'), ('high', 'high')],
                                   help_text='Queue name', max_length=16, verbose_name='queue'),
        ),
        migrations.AlterField(
            model_name='cronjob',
            name='repeat',
            field=models.PositiveIntegerField(blank=True,
                                              help_text='Number of times to run the job. Leaving this blank means it will run forever.',
                                              null=True, verbose_name='repeat'),
        ),
        migrations.AlterField(
            model_name='cronjob',
            name='result_ttl',
            field=models.IntegerField(blank=True,
                                      help_text='The TTL value (in seconds) of the job result.<br/>\n               -1: Result never expires, you should delete jobs manually. <br/>\n                0: Result gets deleted immediately. <br/>\n                >0: Result expires after n seconds.',
                                      null=True, verbose_name='result ttl'),
        ),
        migrations.AlterField(
            model_name='repeatablejob',
            name='at_front',
            field=models.BooleanField(blank=True, default=False,
                                      help_text='When queuing the job, add it in the front of the queue', null=True,
                                      verbose_name='At front'),
        ),
        migrations.AlterField(
            model_name='repeatablejob',
            name='enabled',
            field=models.BooleanField(default=True,
                                      help_text='Should job be scheduled? This field is useful to keep past jobs that should no longer be scheduled',
                                      verbose_name='enabled'),
        ),
        migrations.AlterField(
            model_name='repeatablejob',
            name='job_id',
            field=models.CharField(blank=True, editable=False, help_text='Current job_id on queue', max_length=128,
                                   null=True, verbose_name='job id'),
        ),
        migrations.AlterField(
            model_name='repeatablejob',
            name='queue',
            field=models.CharField(choices=[('default', 'default'), ('low', 'low'), ('high', 'high')],
                                   help_text='Queue name', max_length=16, verbose_name='queue'),
        ),
        migrations.AlterField(
            model_name='repeatablejob',
            name='repeat',
            field=models.PositiveIntegerField(blank=True,
                                              help_text='Number of times to run the job. Leaving this blank means it will run forever.',
                                              null=True, verbose_name='repeat'),
        ),
        migrations.AlterField(
            model_name='repeatablejob',
            name='result_ttl',
            field=models.IntegerField(blank=True,
                                      help_text='The TTL value (in seconds) of the job result.<br/>\n               -1: Result never expires, you should delete jobs manually. <br/>\n                0: Result gets deleted immediately. <br/>\n                >0: Result expires after n seconds.',
                                      null=True, verbose_name='result ttl'),
        ),
        migrations.AlterField(
            model_name='scheduledjob',
            name='at_front',
            field=models.BooleanField(blank=True, default=False,
                                      help_text='When queuing the job, add it in the front of the queue', null=True,
                                      verbose_name='At front'),
        ),
        migrations.AlterField(
            model_name='scheduledjob',
            name='enabled',
            field=models.BooleanField(default=True,
                                      help_text='Should job be scheduled? This field is useful to keep past jobs that should no longer be scheduled',
                                      verbose_name='enabled'),
        ),
        migrations.AlterField(
            model_name='scheduledjob',
            name='job_id',
            field=models.CharField(blank=True, editable=False, help_text='Current job_id on queue', max_length=128,
                                   null=True, verbose_name='job id'),
        ),
        migrations.AlterField(
            model_name='scheduledjob',
            name='queue',
            field=models.CharField(choices=[('default', 'default'), ('low', 'low'), ('high', 'high')],
                                   help_text='Queue name', max_length=16, verbose_name='queue'),
        ),
        migrations.AlterField(
            model_name='scheduledjob',
            name='result_ttl',
            field=models.IntegerField(blank=True,
                                      help_text='The TTL value (in seconds) of the job result.<br/>\n               -1: Result never expires, you should delete jobs manually. <br/>\n                0: Result gets deleted immediately. <br/>\n                >0: Result expires after n seconds.',
                                      null=True, verbose_name='result ttl'),
        ),
    ]
