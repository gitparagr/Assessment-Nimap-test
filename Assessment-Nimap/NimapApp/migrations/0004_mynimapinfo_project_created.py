# Generated by Django 4.0.6 on 2022-07-12 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NimapApp', '0003_remove_mynimapinfo_client_mynimapinfo_project_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mynimapinfo',
            name='project_created',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
