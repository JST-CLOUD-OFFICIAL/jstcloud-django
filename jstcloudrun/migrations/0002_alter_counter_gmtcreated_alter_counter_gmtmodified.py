# Generated by Django 4.1.7 on 2023-04-03 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jstcloudrun', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counter',
            name='gmtCreated',
            field=models.DateTimeField(auto_now_add=True, db_column='gmt_created'),
        ),
        migrations.AlterField(
            model_name='counter',
            name='gmtModified',
            field=models.DateTimeField(auto_now=True, db_column='gmt_modified'),
        ),
    ]
