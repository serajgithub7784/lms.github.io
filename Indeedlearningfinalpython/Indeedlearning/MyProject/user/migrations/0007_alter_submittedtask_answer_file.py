# Generated by Django 3.2.4 on 2023-09-23 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_submittedtask'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submittedtask',
            name='answer_file',
            field=models.FileField(null=True, upload_to='static/submittedtask'),
        ),
    ]
