# Generated by Django 4.0.1 on 2022-01-06 20:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('scheduler', '0001_initial_squashed_0005_added_result_ttl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cronjob',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='repeatablejob',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='scheduledjob',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
