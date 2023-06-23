# Generated by Django 4.1.7 on 2023-03-12 19:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('scheduler', '0008_rename_str_val_jobarg_val_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobarg',
            name='arg_type',
            field=models.CharField(
                choices=[('str', 'string'), ('int', 'int'), ('bool', 'boolean'), ('datetime', 'datetime'),
                         ('callable', 'callable')], default='str', max_length=12, verbose_name='Argument Type'),
        ),
        migrations.AlterField(
            model_name='jobarg',
            name='val',
            field=models.CharField(blank=True, max_length=255, verbose_name='Argument Value'),
        ),
        migrations.AlterField(
            model_name='jobkwarg',
            name='arg_type',
            field=models.CharField(
                choices=[('str', 'string'), ('int', 'int'), ('bool', 'boolean'), ('datetime', 'datetime'),
                         ('callable', 'callable')], default='str', max_length=12, verbose_name='Argument Type'),
        ),
        migrations.AlterField(
            model_name='jobkwarg',
            name='val',
            field=models.CharField(blank=True, max_length=255, verbose_name='Argument Value'),
        ),
    ]
