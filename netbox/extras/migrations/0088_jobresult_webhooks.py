# Generated by Django 4.1.7 on 2023-02-28 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0087_dashboard'),
    ]

    operations = [
        migrations.AddField(
            model_name='webhook',
            name='type_job_end',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='webhook',
            name='type_job_start',
            field=models.BooleanField(default=False),
        ),
    ]
