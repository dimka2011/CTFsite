# Generated by Django 5.1.2 on 2024-10-20 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stf', '0010_rename_userwins_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='solved_tasks',
            field=models.CharField(default='', max_length=10000000),
        ),
    ]
